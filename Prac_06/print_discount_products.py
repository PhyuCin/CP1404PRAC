"""Print only the products with discount(True)"""

products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]

for i in range(len(products)):
    if products[i][2] is True:
        print(*products[i], sep=", ")
