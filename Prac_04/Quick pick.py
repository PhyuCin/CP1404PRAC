import random

SMALLEST = 1
LARGEST = 45
numbers = []
quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks):
    for n in range(6):
        number = random.randrange(SMALLEST, LARGEST + 1)
        TorF = number in numbers
        while TorF is True:
            number = random.randrange(SMALLEST, LARGEST + 1)
            TorF = number in numbers
        print("{:4}".format(number), end="")
        numbers.append(number)
    print()