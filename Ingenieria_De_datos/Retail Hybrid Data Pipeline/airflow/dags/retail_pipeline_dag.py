from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import os
import kagglehub
import pandas as pd

# Funciones del pipeline
#
def extract_transform_load():
    proyect_data_dir = "data"
    dataset_ID = "carrie1/ecommerce-data"
    F_Sales_path = os.path.join(proyect_data_dir, "sales.csv")
    F_Customers_path = os.path.join(proyect_data_dir, "customers.json")

    os.makedirs(proyect_data_dir, exist_ok=True)

    print("Descargando dataset desde Kaggle...")
    path = kagglehub.dataset_download(dataset_ID)

    source_csv = None
    for file in os.listdir(path):
        if file.endswith(".csv"):
            source_csv = os.path.join(path, file)
            break

    if not source_csv:
        raise FileNotFoundError("No se encontró archivo CSV en el dataset descargado.")

    print(f"Dataset descargado: {source_csv}")

    print("Limpiando y preparando datos de ventas...")
    df = pd.read_csv(source_csv, encoding="latin1")
    df = df.dropna(subset=["CustomerID"])
    df = df.rename(columns={
        "InvoiceNo": "sale_id",
        "CustomerID": "customer_id",
        "Description": "product",
        "Quantity": "quantity",
        "UnitPrice": "price",
        "InvoiceDate": "date",
        "Country": "country"
    })
    df = df[["sale_id", "customer_id", "product", "quantity", "price", "date", "country"]]
    df.to_csv(F_Sales_path, index=False)
    print(f"Archivo de ventas guardado en: {F_Sales_path}")

    print("Generando archivo customers.json...")
    customers = (
        df[["customer_id", "country"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    customers["name"] = customers["customer_id"].apply(lambda x: f"Customer_{int(x)}")
    customers["email"] = customers["name"].apply(lambda x: f"{x.lower()}@example.com")
    customers["loyalty_level"] = customers["customer_id"].apply(
        lambda x: "Gold" if int(x) % 5 == 0 else "Silver"
    )
    customers.to_json(F_Customers_path, orient="records", indent=2)
    print(f"Archivo de clientes guardado en: {F_Customers_path}")

    print("Pipeline completado exitosamente.")


# DEFINICIon DAG

default_args = {
    'owner': 'Adan',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='retail_pipeline_dag',
    default_args=default_args,
    description='Pipeline ETL para datos de ventas minoristas',
    schedule_interval='@daily',  # ejecutar una vez al día
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['retail', 'etl', 'kaggle']
) as dag:

    run_etl = PythonOperator(
        task_id='extract_transform_load',
        python_callable=extract_transform_load
    )

    run_etl
