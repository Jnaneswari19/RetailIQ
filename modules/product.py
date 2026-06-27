import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql@1234",
        database="retailiq"
    )


def add_product(name, category, price, stock):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO products
    (product_name, category, price, stock_quantity)
    VALUES (%s, %s, %s, %s)
    """

    values = (name, category, price, stock)

    cursor.execute(query, values)
    connection.commit()

    print("Product Added Successfully")

    cursor.close()
    connection.close()


add_product(
    "Gaming Mouse",
    "Accessories",
    1200,
    50
)
def view_products():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()


view_products()
def search_product(product_name):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT * FROM products
    WHERE product_name = %s
    """

    cursor.execute(query, (product_name,))

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()


search_product("Laptop")
def update_stock(product_id, new_stock):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE products
    SET stock_quantity = %s
    WHERE product_id = %s
    """

    cursor.execute(query, (new_stock, product_id))
    connection.commit()

    print("Stock Updated Successfully")

    cursor.close()
    connection.close()


update_stock(1, 100)
