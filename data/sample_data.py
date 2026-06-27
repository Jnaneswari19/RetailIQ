import random
from datetime import datetime, timedelta

from database.database import Database

db = Database()


def generate_customers():

    cities = [
        "Hyderabad",
        "Bangalore",
        "Mumbai",
        "Delhi",
        "Chennai"
    ]

    regions = [
        "South",
        "North",
        "West"
    ]

    customers = []

    for i in range(1, 51):

        customers.append(
            (
                f"Customer_{i}",
                f"customer{i}@gmail.com",
                f"98765{i:05}",
                random.choice(cities),
                random.choice(regions),
                datetime.now().date()
            )
        )

    db.execute_many(
        """
        INSERT INTO Customers
        (
            customer_name,
            email,
            phone,
            city,
            region,
            join_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        customers
    )

    print("50 Customers Inserted")


def generate_products():

    categories = [
        "Electronics",
        "Accessories",
        "Furniture",
        "Fashion",
        "Home Appliances"
    ]

    products = []

    for i in range(1, 101):

        cost_price = random.randint(100, 5000)

        selling_price = cost_price + random.randint(50, 1500)

        stock_quantity = random.randint(20, 500)

        products.append(
            (
                f"Product_{i}",
                random.choice(categories),
                cost_price,
                selling_price,
                stock_quantity
            )
        )

    db.execute_many(
        """
        INSERT INTO Products
        (
            product_name,
            category,
            cost_price,
            selling_price,
            stock_quantity
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        products
    )

    print("100 Products Inserted")


def generate_orders():

    orders = []

    start_date = datetime(2025, 1, 1)

    for _ in range(500):

        customer_id = random.randint(1, 50)

        order_date = start_date + timedelta(
            days=random.randint(0, 365)
        )

        total_amount = random.randint(
            500,
            25000
        )

        orders.append(
            (
                customer_id,
                order_date.date(),
                total_amount
            )
        )

    db.execute_many(
        """
        INSERT INTO Orders
        (
            customer_id,
            order_date,
            total_amount
        )
        VALUES (?, ?, ?)
        """,
        orders
    )

    print("500 Orders Inserted")


def generate_sales():

    sales = []

    for order_id in range(1, 501):

        product_id = random.randint(1, 100)

        quantity = random.randint(1, 10)

        product = db.fetch_one(
            """
            SELECT
                cost_price,
                selling_price
            FROM Products
            WHERE product_id = ?
            """,
            (product_id,)
        )

        cost_price = product[0]
        selling_price = product[1]

        revenue = quantity * selling_price

        profit = revenue - (quantity * cost_price)

        sales.append(
            (
                order_id,
                product_id,
                quantity,
                selling_price,
                revenue,
                profit
            )
        )

    db.execute_many(
        """
        INSERT INTO Sales
        (
            order_id,
            product_id,
            quantity,
            unit_price,
            revenue,
            profit
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        sales
    )

    print("500 Sales Records Inserted")


if __name__ == "__main__":

    generate_customers()

    generate_products()

    generate_orders()

    generate_sales()

    print("\nDataset Generation Completed")