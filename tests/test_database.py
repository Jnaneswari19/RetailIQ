from database.database import Database

db = Database()

print("\nTesting Database Layer\n")

customer = db.fetch_one(
    """
    SELECT customer_name
    FROM Customers
    LIMIT 1
    """
)

print("First Customer:")
print(customer)

total_customers = db.fetch_one(
    """
    SELECT COUNT(*)
    FROM Customers
    """
)

print("\nCustomer Count:")
print(total_customers[0])

products = db.fetch_all(
    """
    SELECT product_name
    FROM Products
    LIMIT 5
    """
)

print("\nFirst 5 Products:")

for product in products:
    print(product[0])