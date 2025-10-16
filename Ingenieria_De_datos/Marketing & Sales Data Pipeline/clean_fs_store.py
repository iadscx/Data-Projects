import pandas as pd
import json
from datetime import datetime

# 1. Leer los archivos JSON

users = pd.read_json("users.json")
products = pd.read_json("products.json")

# carts tiene estructura más compleja (listas anidadas)
with open("carts.json", "r") as f:
    carts_data = json.load(f)

# LIMPIEZA: Customers

customers = pd.DataFrame({
    "name": users["name"].apply(lambda x: f"{x['firstname']} {x['lastname']}"),
    "email": users["email"].str.lower(),
    "city": users["address"].apply(lambda x: x["city"]),
    "country": ["USA"] * len(users),  # Fake Store no tiene país
    "registration_date": datetime.now().strftime("%Y-%m-%d")
})

customers.to_csv("customers.csv", index=False)
print("customers.csv created successfully")

# LIMPIEZA: Campaigns (Products)

campaigns = pd.DataFrame({
    "name": products["title"],
    "start_date": "2025-01-01",
    "end_date": "2025-12-31",
    "budget": products["price"] * 10  # presupuesto simulado
})

campaigns.to_csv("campaigns.csv", index=False)
print("campaigns.csv created successfully")

# LIMPIEZA: Sales (Carts)

sales_records = []
for cart in carts_data:
    customer_id = cart["userId"]
    sale_date = cart["date"]
    for product in cart["products"]:
        campaign_id = product["productId"]
        quantity = product["quantity"]
        amount = quantity * 20  # precio simulado
        sales_records.append({
            "customer_id": customer_id,
            "campaign_id": campaign_id,
            "amount": amount,
            "sale_date": sale_date
        })

sales = pd.DataFrame(sales_records)
sales.to_csv("sales.csv", index=False)
print("sales.csv created successfully")

print("\nAll CSV files are ready to import into PostgreSQL")
