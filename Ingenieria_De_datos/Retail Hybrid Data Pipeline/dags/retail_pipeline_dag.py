from airflow import DAG
from airflow.operators.python  import PythonOperator
from datetime import datetime
from pipelines.mysql_pipeline import load_sales_to_mysql
from pipelines.mongodb_pipeline import load_customers_to_mongodb
from pipelines.hybrid_pipeline import hybrid_processing

default_args = {
    'owner': 'Adan',
    'start_date': datetime(2025, 10, 16),
    'retries': 1
}

dag = DAG('retail_hybrid_pipeline', default_args=default_args, schedule_interval='@daily')

task_mysql = PythonOperator(task_id='load_sales', python_callable=load_sales_to_mysql, dag=dag)
task_mongo = PythonOperator(task_id='load_customers', python_callable=load_customers_to_mongodb, dag=dag)
task_hybrid = PythonOperator(task_id='process_hybrid', python_callable=hybrid_processing, dag=dag)

task_mysql >> task_mongo >> task_hybrid
