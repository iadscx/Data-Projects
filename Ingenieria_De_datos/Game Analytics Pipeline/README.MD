Game Analytics Pipeline

## Descripción

Este proyecto es un **pipeline de análisis de datos de Fortnite y Steam**, construido con tecnologías de Big Data y orquestación profesional. Permite **extraer estadísticas de jugadores desde la API de Steam**, procesarlas y cargarlas en almacenamiento escalable para análisis y visualización.

El pipeline incluye:

- **Extracción de datos**: Desde la API de Steam y Fortnite.
- **Transformación de datos**: Procesamiento distribuido usando PySpark.
- **Carga de datos**: Almacenamiento en MinIO (simulación de S3) y BigQuery para análisis y consultas.
- **Orquestación**: Apache Airflow maneja la ejecución automatizada de todas las tareas.
- **Contenedores**: Docker y Docker Compose para reproducibilidad en cualquier entorno.

**Objetivo**: Integración de Big Data, APIs externas y automatización de pipelines en un entorno local profesional, con posibilidad de escalar a producción en la nube.

---

## Tecnologías utilizadas

- **Lenguaje**: Python 
- **Orquestación**: Apache Airflow 
- **Procesamiento distribuido**: PySpark
- **Almacenamiento en la nube**: MinIO (local S3) y Google BigQuery
- **Bases de datos**: MongoDB
- **Gestión de dependencias**: `requirements.txt`
- **Contenedores**: Docker
- **Gestión de variables sensibles**: `.env`

---

## Estructura del proyecto

fortnite_steam_pipeline/
│
├── dags/ # DAGs de Airflow
├── scripts/ # Extractor, Transformer, Loader
├── plugins/ # Operadores
├── config/ # Configuración de parámetros
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
