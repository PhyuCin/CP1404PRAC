import random
SMALLEST = 1
LARGEST = 45
numbers = [1,2,3,4,5,5,6,6]

#for i in range(0, 10):
    #num = random.randrange(SMALLEST, LARGEST + 1)
    #while num in numbers is False:
        #number = random.randrange(SMALLEST, LARGEST + 1)
    #numbers.append(num)
num = int(input("Number: "))
print(num not in numbers)
TorF = num in numbers
while TorF is False:
    num = int(input("Number again: "))

print("True")