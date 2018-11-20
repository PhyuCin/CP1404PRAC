price_list = []
num_of_items = int(input("Number of items: "))

while num_of_items < 0:
    print("Invalid number of items!")
    num_of_items = int(input("Number of items: "))

print()
for i in range(0, num_of_items):
    price = float(input("Price of item: "))
    while price < 0:
        print("Invalid price!")
        price = float(input("Price of item: "))
    price_list.append(price)

total_price = sum(price_list)

if total_price > 100:
    total_price = total_price * 0.9
    print("Total price for", num_of_items, "items is ${:.2f}.".format(total_price))

else:
    print("Total price for", num_of_items, "items is ${:.2f}.".format(total_price))

