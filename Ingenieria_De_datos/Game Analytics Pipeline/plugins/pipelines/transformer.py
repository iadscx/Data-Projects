from pyspark.sql import SparkSession
import json

def transform_data():
    print("Iniciando sesión PySpark")
    spark = SparkSession.builder.appName("FortniteTransform").getOrCreate()

    df = spark.read.json("data/raw_data.json")
    df_clean = df.selectExpr("explode(applist.apps) as app") \
                 .select("app.appid", "app.name") \
                 .dropna()

    df_clean.write.mode("overwrite").json("data/processed_data")
    print("Datos transformados y guardados en data/processed_data")
    spark.stop()
