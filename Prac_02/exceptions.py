try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    print("Finished.")

finished = False
result = 0
while not finished:
    try:
        num = int(input("Enter a number: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
        print("Valid result is:", result)

