numbers = []

for i in range(0, 5):
    num = int(input("Number: "))
    numbers.append(num)
print("The first number is", numbers[0])
print("The first number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))

average = sum(numbers)/len(numbers)

print("The average of the numbers is {:.2}".format(average))


