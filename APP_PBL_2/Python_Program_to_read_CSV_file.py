import csv
import os

sales = {}

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "sales.csv"
)

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["Product"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        amount = quantity * price

        if product in sales:
            sales[product] += amount
        else:
            sales[product] = amount

print("Total Sales Amount for Each Product:")

for product in sales:
    print(product, ":", sales[product])