age = int(input("Enter age: "))

count = 0
total = 0
while age > 0 and age < 130:
    count += 1
    total += age
    age = int(input("Enter age: "))

average = total/count
print("The average age is {:.2f}".format(average))