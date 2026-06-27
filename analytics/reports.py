import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# =====================================
# Database Connection
# =====================================

username = "root"
password = quote_plus("Mysql@1234")   # Your MySQL password
host = "localhost"
port = "3306"
database = "retailiq"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# =====================================
# SQL Query
# =====================================

query = """
SELECT
    s.sale_id,
    c.customer_name,
    p.product_name,
    s.quantity,
    s.sale_date,
    s.total_amount
FROM sales s
JOIN customers c
    ON s.customer_id = c.customer_id
JOIN products p
    ON s.product_id = p.product_id;
"""

# =====================================
# Read Data
# =====================================

df = pd.read_sql(query, engine)

print("\n========== SALES REPORT ==========\n")
print(df)

# =====================================
# Monthly Sales Report
# =====================================

df["sale_date"] = pd.to_datetime(df["sale_date"])

monthly_sales = (
    df.groupby(df["sale_date"].dt.to_period("M"))["total_amount"]
    .sum()
    .reset_index()
)

monthly_sales["sale_date"] = monthly_sales["sale_date"].astype(str)

print("\n========== MONTHLY SALES ==========\n")
print(monthly_sales)

# =====================================
# Top 5 Customers
# =====================================

top_customers = (
    df.groupby("customer_name", as_index=False)["total_amount"]
    .sum()
    .sort_values(by="total_amount", ascending=False)
    .head(5)
)

print("\n========== TOP 5 CUSTOMERS ==========\n")
print(top_customers)

# =====================================
# Top 5 Products
# =====================================

top_products = (
    df.groupby("product_name", as_index=False)["quantity"]
    .sum()
    .sort_values(by="quantity", ascending=False)
    .head(5)
)

print("\n========== TOP 5 PRODUCTS ==========\n")
print(top_products)

# =====================================
# Overall Statistics
# =====================================

print("\n========== SUMMARY ==========\n")
print(f"Total Sales Records : {len(df)}")
print(f"Total Revenue       : ₹{df['total_amount'].sum():,.2f}")
print(f"Average Sale Value  : ₹{df['total_amount'].mean():,.2f}")

# =====================================
# Export Reports to CSV
# =====================================

monthly_sales.to_csv("monthly_sales_report.csv", index=False)
top_customers.to_csv("top_customers_report.csv", index=False)
top_products.to_csv("top_products_report.csv", index=False)

print("\nReports exported successfully!")
print("Generated files:")
print("1. monthly_sales_report.csv")
print("2. top_customers_report.csv")
print("3. top_products_report.csv")