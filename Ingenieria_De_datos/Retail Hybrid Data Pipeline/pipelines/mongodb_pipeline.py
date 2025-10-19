import json
from config.mongodb_config import db

def load_customers_to_mongodb(file_path="data/customers.json"):
    with open(file_path) as f:
        data = json.load(f)
    collection = db["customers"]
    collection.insert_many(data)
    print("Datos de clientes cargados en MongoDB")
