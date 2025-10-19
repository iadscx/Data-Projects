# Retail Hybrid Data Pipeline

## Descripción del proyecto
Este proyecto implementa un **pipeline de datos híbrido (local + nube)** que integra bases de datos relacionales y no relacionales para gestionar información de ventas y comportamiento del cliente.  
El objetivo es demostrar la construcción de un flujo de datos completo, escalable y automatizado, combinando extracción, transformación, carga (ETL) y orquestación de tareas.

El pipeline permite:
- Manejar datos estructurados (MySQL) y no estructurados (MongoDB).
- Procesar grandes volúmenes de información mediante **PySpark**.
- Almacenar los datos procesados en **AWS S3**.
- Automatizar la ejecución del flujo de trabajo con **Apache Airflow** usando contenedores Docker.

---

## Tecnologías utilizadas
| Componente | Tecnología | Descripción |
|------------|------------|------------|
| Base de datos relacional | MySQL | Almacenamiento de datos estructurados de ventas |
| Base de datos NoSQL | MongoDB | Almacenamiento de datos semiestructurados sobre comportamiento del cliente |
| Procesamiento distribuido | PySpark | Limpieza, transformación y análisis de datos |
| Orquestación | Apache Airflow (Docker) | Automatización y monitoreo de tareas ETL |
| Almacenamiento en la nube | AWS S3 | Centralización y persistencia de datos procesados |
| Lenguaje | Python | Integración y procesamiento de datos |
| Control de versiones | Git | Versionamiento del proyecto y portafolio profesional |

---

## Estructura del proyecto
Retail Hybrid Data Pipeline/
│
├── dags/ # DAGs de Airflow
├── logs/ # Logs por Airflow
├── plugins/ # Plugins
├── data/ 
├── scripts/ # Scripts ETL
├── requirements.txt 
├── Dockerfile 
└── docker-compose.yml 
