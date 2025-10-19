import kagglehub
import os
import shutil
import pandas as pd
import json

# CONFIGURACIONES

proyect_data_dir = "data"
dataset_ID = "carrie1/ecommerce-data"
F_Sales_path = os.path.join(proyect_data_dir, "sales.csv")
F_Customers_path = os.path.join(proyect_data_dir, "customers.json")

# Crear carpeta data si no existe
os.makedirs(proyect_data_dir, exist_ok=True)

# EXTRACCIÓN

print("Descargando dataset desde Kaggle...")
path = kagglehub.dataset_download(dataset_ID)

# Buscar archivo principal (data.csv)
source_csv = None
for file in os.listdir(path):
    if file.endswith(".csv"):
        source_csv = os.path.join(path, file)
        break

if not source_csv:
    raise FileNotFoundError("No se encontró archivo CSV en el dataset descargado.")

print(f"Dataset descargado: {source_csv}")

# Transofmracion
print("Limpiando y preparando datos de ventas...")

# Leer CSV 
df = pd.read_csv(source_csv, encoding="latin1")

# Eliminar filas sin ID de cliente
df = df.dropna(subset=["CustomerID"])

# Renombrar columnas para pipeline
df = df.rename(columns={
    "InvoiceNo": "sale_id",
    "CustomerID": "customer_id",
    "Description": "product",
    "Quantity": "quantity",
    "UnitPrice": "price",
    "InvoiceDate": "date",
    "Country": "country"
})

# Seleccionar columnas relevantes
df = df[["sale_id", "customer_id", "product", "quantity", "price", "date", "country"]]

# CARGA: Guardar CSV limpio
#
df.to_csv(F_Sales_path, index=False)
print(f" Archivo de ventas guardado en: {F_Sales_path}")

# Creacion customers.JSON

print("Generando archivo customers.json...")

customers = (
    df[["customer_id", "country"]]
    .drop_duplicates()
    .reset_index(drop=True)
)

# Agregar información simulada de cliente
customers["name"] = customers["customer_id"].apply(lambda x: f"Customer_{int(x)}")
customers["email"] = customers["name"].apply(lambda x: f"{x.lower()}@example.com")
customers["loyalty_level"] = customers["customer_id"].apply(
    lambda x: "Gold" if int(x) % 5 == 0 else "Silver"
)

# Guardar en JSON
customers.to_json(F_Customers_path, orient="records", indent=2)

print(f"Archivo de clientes guardado en: {F_Customers_path}")

# FINAL

print("Extracción y preparación de datos completada exitosamente.")
print(f"Archivos listos:\n - {F_Sales_path}\n - {F_Customers_path}")
