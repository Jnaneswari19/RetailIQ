import mysql.connector


def add_customer(name, email, phone, city):

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql@1234",
        database="retailiq"
    )

    cursor = connection.cursor()

    query = """
    INSERT INTO customers
    (customer_name, email, phone, city)
    VALUES (%s,%s,%s,%s)
    """

    values = (name, email, phone, city)

    cursor.execute(query, values)

    connection.commit()

    print("Customer Added Successfully")

    cursor.close()
    connection.close()


add_customer(
    "Kiran Kumar",
    "kiran@gmail.com",
    "9999999999",
    "Hyderabad"
)
def view_customers():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="retailiq"
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM customers")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()


view_customers()