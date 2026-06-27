from modules.customer import Customer

customer = Customer()

print("\nCUSTOMER MODULE TEST\n")


print("1. VIEW FIRST 5 CUSTOMERS\n")

customers = customer.view_customers()

for row in customers[:5]:
    print(row)


print("\n2. SEARCH CUSTOMER ID = 1\n")

result = customer.search_customer(1)

print(result)


print("\n3. ADD NEW CUSTOMER\n")

new_customer_id = customer.add_customer(
    "John Smith",
    "johnsmith@test.com",
    "9999999999",
    "Hyderabad",
    "South",
    "2025-06-25"
)

print("Inserted Customer ID:", new_customer_id)


print("\n4. SEARCH NEW CUSTOMER\n")

result = customer.search_customer(
    new_customer_id
)

print(result)


print("\n5. UPDATE CUSTOMER\n")

updated_rows = customer.update_customer(
    new_customer_id,
    "John Updated",
    "johnupdated@test.com",
    "8888888888",
    "Bangalore",
    "South"
)

print("Rows Updated:", updated_rows)


print("\n6. SEARCH UPDATED CUSTOMER\n")

result = customer.search_customer(
    new_customer_id
)

print(result)


print("\n7. DELETE CUSTOMER\n")

deleted_rows = customer.delete_customer(
    new_customer_id
)

print("Rows Deleted:", deleted_rows)


print("\n8. VERIFY DELETE\n")

result = customer.search_customer(
    new_customer_id
)

print(result)