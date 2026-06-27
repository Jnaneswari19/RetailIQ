import mysql.connector
from datetime import date


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql@1234",
        database="retailiq"
    )


def add_sale(customer_id, product_id, quantity):

    connection = get_connection()
    cursor = connection.cursor()

    # Get product price and stock
    cursor.execute(
        "SELECT price, stock_quantity FROM products WHERE product_id=%s",
        (product_id,)
    )

    product = cursor.fetchone()

    if not product:
        print("Product not found")
        return

    price, stock = product

    if quantity > stock:
        print("Insufficient stock")
        return

    total_amount = price * quantity

    # Insert sale
    cursor.execute("""
        INSERT INTO sales
        (customer_id, product_id, quantity, sale_date, total_amount)
        VALUES (%s,%s,%s,%s,%s)
    """, (customer_id, product_id, quantity, date.today(), total_amount))

    # Update stock
    cursor.execute("""
        UPDATE products
        SET stock_quantity = stock_quantity - %s
        WHERE product_id = %s
    """, (quantity, product_id))

    connection.commit()

    print("Sale Recorded Successfully")

    cursor.close()
    connection.close()


add_sale(1, 1, 2)
def view_sales():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT
        s.sale_id,
        c.customer_name,
        p.product_name,
        s.quantity,
        s.total_amount
    FROM sales s
    JOIN customers c
        ON s.customer_id = c.customer_id
    JOIN products p
        ON s.product_id = p.product_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()


view_sales()
