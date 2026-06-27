import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Mysql@1234",
    host="localhost",
    database="retailiq"
)

engine = create_engine(url)

df = pd.read_sql("SELECT * FROM sales", engine)

print(df)
print("\nTotal Sales Records:", len(df))

print("\nTotal Revenue:")
print(df["total_amount"].sum())

print("\nAverage Sale Value:")
print(df["total_amount"].mean())
customer_sales = pd.read_sql("""
SELECT
    c.customer_name,
    SUM(s.total_amount) AS revenue
FROM sales s
JOIN customers c
ON s.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY revenue DESC
""", engine)

print("\nTop Customers")
print(customer_sales)
product_sales = pd.read_sql("""
SELECT
    p.product_name,
    SUM(s.quantity) AS total_sold
FROM sales s
JOIN products p
ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
""", engine)

print("\nTop Products")
print(product_sales)

import matplotlib.pyplot as plt

product_sales.plot(
    x="product_name",
    y="total_sold",
    kind="bar",
    legend=False
)

plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()

plt.show()