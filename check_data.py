from database.database import Database

db = Database()

tables = [
    "Customers",
    "Products",
    "Orders",
    "Sales"
]

for table in tables:

    count = db.fetch_one(
        f"SELECT COUNT(*) FROM {table}"
    )[0]

    print(table, count)