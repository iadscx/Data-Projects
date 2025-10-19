import boto3
import os

def load_data():
    print("Cargando datos procesados a MinIO (simulador de S3)")
    s3 = boto3.client(
        's3',
        endpoint_url='http://minio:9000',
        aws_access_key_id='minioadmin',
        aws_secret_access_key='minioadmin'
    )

    bucket = 'fortnite-data'
    s3.create_bucket(Bucket=bucket)

    for root, dirs, files in os.walk("data/processed_data"):
        for file in files:
            path = os.path.join(root, file)
            s3.upload_file(path, bucket, file)
    print("Datos cargados en bucket S3:")
