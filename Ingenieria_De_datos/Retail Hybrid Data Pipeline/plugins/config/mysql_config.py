from sqlalchemy import create_engine

MYSQL_USER = "root"
MYSQL_PASSWORD = "xlr80010"
MYSQL_HOST = "host.docker.internal"
MYSQL_PORT = "3306"
MYSQL_DB = "retail_sales"

engine = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}")
