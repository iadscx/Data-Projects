import pandas as pd
from config.mysql_config import engine

def load_sales_to_mysql(file_path="data/sales.csv"):
    df = pd.read_csv(file_path)
    df.to_sql('sales', con=engine, if_exists='replace', index=False)
    print("Datos de ventas cargados en MySQL")
