numbers = []
num = 0
i = 1
while not num < 0:
    num = int(input("Number {}: ".format(i)))
    i += 1
    numbers.append(num)
del numbers[-1]
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))

average = sum(numbers)/(len(numbers))
print(numbers)
print("The average of the numbers is {:.2}".format(average))

