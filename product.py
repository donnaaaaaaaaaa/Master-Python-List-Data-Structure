

# List of product dictionaries
products = [
    {"name": "Laptop", "category": "Electronics", "price": 750, "stock": 50, "supplier_email": "supplier1@gmail.com"},
    {"name": "Desk Chair", "category": "Furniture", "price": 100, "stock": 200, "supplier_email": "supplier2@gmail.com"},
    {"name": "Smartwatch", "category": "Electronics", "price": 200, "stock": 150, "supplier_email": "supplier3@gmail.com"},
    {"name": "Notebook", "category": "Stationery", "price": 5, "stock": 500, "supplier_email": "supplier4@gmail.com"},
    {"name": "Running Shoes", "category": "Apparel", "price": 80, "stock": 100, "supplier_email": "supplier5@gmail.com"}
]

print("Products:")
for product in products:
    print(f"Name: {product['name']}, Category: {product['category']}, Price: {product['price']}, Stock: {product['stock']}, Supplier Email: {product['supplier_email']}")