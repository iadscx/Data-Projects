from pyspark.sql import SparkSession
from config.mysql_config import engine
from config.mongodb_config import db
import pandas as pd

def hybrid_processing():
    spark = SparkSession.builder.appName("RetailHybridPipeline").getOrCreate()
    
    # Leer datos de MySQL
    sales_df = pd.read_sql("SELECT * FROM sales", con=engine)
    sales_spark = spark.createDataFrame(sales_df)
    
    # Leer datos de MongoDB
    customers = list(db.customers.find())
    customers_df = pd.DataFrame(customers)
    customers_spark = spark.createDataFrame(customers_df)
    
    # Hacer join por customer_id
    hybrid_df = sales_spark.join(customers_spark, sales_spark.customer_id == customers_spark.customer_id, "inner")
    
    hybrid_df.show(10)
    
    return hybrid_df
