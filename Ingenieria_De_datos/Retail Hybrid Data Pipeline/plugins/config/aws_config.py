import boto3

AWS_ACCESS_KEY = "TU_ACCESS_KEY"
AWS_SECRET_KEY = "TU_SECRET_KEY"
AWS_REGION = "us-east-1"
S3_BUCKET = "retail-hybrid-data"

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)
