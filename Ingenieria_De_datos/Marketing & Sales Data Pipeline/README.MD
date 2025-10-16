El pproyecto se llama: Marketing & Sales Data Pipeline

Este proyecto demuestra la construcción de un pipeline de datos completo aplicado a marketing y ventas.
Los datos provienen de datasets simulados de clientes, productos y ventas, y se procesan para generar información estructurada lista para análisis.
Se realiza extracción, limpieza, transformación y carga (ETL) en PostgreSQL, preparando los datos para consultas analíticas y 
visualización de métricas clave como ingresos por campaña, top clientes y comportamiento de ventas.

Tecnologías usadas:

-Python: pandas, json, datetime (ETL, limpieza y transformación)
-PostgreSQL: almacenamiento, integración y consultas SQL
-CSV: formato intermedio para unificar datos

Flujo de trabajo / pipeline (ETL)

Extracción:
Lectura de archivos JSON simulados: users.json, products.json, carts.json.

Transformación / Limpieza:
Unificación de nombres de clientes, emails, direcciones.

Normalización de productos como campañas, presupuestos simulados.
Expansión de ventas (cada carrito → línea por producto).

Cálculo de métricas: sale_amount.

Carga:
Creación de una base de datos PostgreSQL (marketing_sales_db).
Creación de tabla marketing_sales con esquema unificado.
Importación del CSV final (marketing_sales_clean.csv).

Análisis / Consultas (SQL):
Top clientes por ingresos
Ingresos por campaña
Ventas por ciudad

Archivos:

Python: 
data_cleaning_pipeline.py 
merge_clean_data.py

Dataset limpio: 
marketing_sales_clean.csv

Script SQL: 
creación de tabla y consultas básicas (marketing_sales.sql)

Screenshots de los datos están cargados y consultas ejecutadas

Diagrama del pipeline: JSON → limpieza Python → CSV → PostgreSQL → análisis SQL
Graficos de ingresos por ciudad, top campañas.
