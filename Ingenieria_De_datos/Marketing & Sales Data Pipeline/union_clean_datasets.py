import pandas as pd

# 1. Cargar los CSV generados
customers = pd.read_csv("customers.csv")
campaigns = pd.read_csv("campaigns.csv")
sales = pd.read_csv("sales.csv")

# 2. Agregar IDs si no existen (por seguridad)
if 'customer_id' not in customers.columns:
    customers['customer_id'] = customers.index + 1
if 'campaign_id' not in campaigns.columns:
    campaigns['campaign_id'] = campaigns.index + 1

# 3. Unir ventas con clientes
merged = sales.merge(customers, on='customer_id', how='left')

# 4. Unir con campañas
merged = merged.merge(campaigns, on='campaign_id', how='left', suffixes=('_customer','_campaign'))

# 5. Crear columnas útiles
merged['revenue_per_sale'] = merged['amount'] / merged['budget'] * 1000

# 6. Reordenar y renombrar columnas
final_df = merged[[
    'customer_id', 'name_customer', 'email', 'city', 'country',
    'campaign_id', 'name_campaign', 'start_date', 'end_date', 'budget',
    'amount', 'sale_date', 'revenue_per_sale'
]]

final_df.rename(columns={
    'name_customer': 'customer_name',
    'name_campaign': 'campaign_name'
}, inplace=True)

# 7. Guardar CSV final
final_df.to_csv("marketing_sales_clean.csv", index=False)
print("Archivo final unificado creado: marketing_sales_clean.csv")
print("Total de filas:", final_df.shape[0])
