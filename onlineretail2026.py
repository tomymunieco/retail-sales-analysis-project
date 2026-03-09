import pandas as pd
df = pd.read_csv('online_retail_II.csv')
df['Customer ID'] = df['Customer ID'].fillna(0).astype(int)
df['Description'] = df['Description'].fillna('Unknown Product').str.strip()
def categorizar(row):
    if row['Price'] < 0:
        return 'Ajuste Contable'
    elif row['Quantity'] < 0:
             return 'Cancelacion'
    else: return 'Venta'
df['Categoria'] = df.apply(categorizar, axis=1)
df['LineTotal'] = df['Price'] * df['Quantity']
dim_customer = df[['Customer ID', 'Country']].drop_duplicates(subset=['Customer ID'])
dim_product = df[['StockCode', 'Description']].drop_duplicates(subset=['StockCode'])
fact_sales = df[['Invoice', 'Customer ID', 'StockCode', 'InvoiceDate', 'Quantity', 'Price', 'LineTotal', 'Categoria']]
dim_customer.to_csv('dim_customer.csv', index=False)
dim_product.to_csv('dim_product.csv', index=False)
fact_sales.to_csv('fact_sales.csv', index=False)    