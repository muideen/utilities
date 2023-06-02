import csv
import random
import datetime

# define constants
MIN_USERS = 39344
MAX_USERS = 4324448
MIN_PRODUCTS = 343
MAX_PRODUCTS = 3404
MIN_ORDERS = 434342839
MAX_ORDERS = 93459348548

# create Users CSV
users = []
for i in range(random.randint(MIN_USERS, MAX_USERS)):
    name = f"User {i}"
    email = f"user{i}@example.com"
    password = "password"
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = created_at
    users.append([name, email, password, created_at, updated_at])

with open('users.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'email', 'password', 'created_at', 'updated_at'])
    writer.writerows(users)

# create Categories CSV
categories = [
    ['Electronics'],
    ['Clothing'],
    ['Home & Garden'],
    ['Toys'],
    ['Books'],
    ['Sports & Outdoors']
]

with open('categories.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'created_at', 'updated_at'])
    writer.writerows(categories)

# create Products CSV
products = []
for i in range(random.randint(MIN_PRODUCTS, MAX_PRODUCTS)):
    name = f"Product {i}"
    description = f"This is product {i}"
    price = round(random.uniform(1, 1000), 2)
    image_url = f"https://example.com/product{i}.jpg"
    category_id = random.randint(1, len(categories))
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = created_at
    products.append([name, description, price, image_url, category_id, created_at, updated_at])

with open('products.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'description', 'price', 'image_url', 'category_id', 'created_at', 'updated_at'])
    writer.writerows(products)

# create Orders and Order_Items CSVs
orders = []
order_items = []
for i in range(random.randint(MIN_ORDERS, MAX_ORDERS)):
    user_id = random.randint(1, len(users))
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = created_at
    orders.append([user_id, created_at, updated_at])
    num_items = random.randint(1, 5)
    for j in range(num_items):
        product_id = random.randint(1, len(products))
        quantity = random.randint(1, 10)
        price = products[product_id-1][2] # get price from products CSV
        order_items.append([i+1, product_id, quantity, price, created_at, updated_at])

with open('orders.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['user_id', 'created_at', 'updated_at'])
    writer.writerows(orders)

with open('order_items.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['order_id', 'product_id', 'quantity', 'price', 'created_at', 'updated_at'])
    writer.writerows(order_items)
