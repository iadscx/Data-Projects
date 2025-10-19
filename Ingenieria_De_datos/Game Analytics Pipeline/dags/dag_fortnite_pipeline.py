from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extractor import extract_data
from scripts.transformer import transform_data
from scripts.loader import load_data

default_args = {
    'owner': 'Adan',
    'start_date': datetime(2025, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='fortnite_analytics_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['fortnite', 'analytics', 'bigdata']
) as dag:

    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    load = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    extract >> transform >> load
