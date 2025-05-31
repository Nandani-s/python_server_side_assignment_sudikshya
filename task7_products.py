import json

with open("products.json","r") as file:
    products = json.load(file)
    
    print(f"{'Name':<15} {'Price':<10} {'Quantity':<10}")
    print("-"* 36)
    
for product in products:
    name = product['name']
    price = product['price']
    quantity = product['quantity']

    print(f"{name:<15} {price:<10} {quantity:<10}")