from pymongo import MongoClient

MONGO_HOST = "host.docker.internal"
MONGO_PORT = 27017
MONGO_DB = "customer_behavior"

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]
