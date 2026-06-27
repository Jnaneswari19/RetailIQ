import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@1234",
    database="retailiq"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()