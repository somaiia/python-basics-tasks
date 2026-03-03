# Q1 - Filter products above price threshold

products = [
    ("Laptop", 1200, 5),
    ("Smartphone", 700, 10),
    ("Headphones", 150, 15),
    ("Monitor", 300, 7)
]

threshold = 500
products_above_threshold = []

for product in products:
    name  = product[0]
    price = product[1]
    if price > threshold:
        products_above_threshold.append(name)

print("products above the price threshold:", products_above_threshold)
