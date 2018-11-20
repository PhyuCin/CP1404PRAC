x = int(input("Enter the smaller number: "))
y = int(input("Enter the bigger number: "))

while x >= y:
    print("Invalid numbers\n")
    x = int(input("Enter smaller number: "))
    y = int(input("Enter bigger number: "))

print("\nMenu:"
      "\n(E)ven numbers from", x, "to", y,
      "\n(O)dd numbers from", x, "to", y,
      "\n(S)quares from", x, "to", y,
      "\n(Q)uit the program")
choice = input(">>> ")
choice = choice.upper()

while choice != "Q":
    if choice == "E":
        if x % 2 == 0:
            print("Even numbers from", x, "to", y, ":")
            for i in range (x,y+1,2):
                print(i)
        else:
            print("Even numbers from", x, "to", y, ":")
            for i in range(x+1, y+1, 2):
                print(i)
    elif choice == "O":
        if x % 2 == 1:
            print("Odd numbers from", x, "to", y, ":")
            for i in range (x,y+1,2):
                print(i)
        else:
            print("Odd numbers from", x, "to", y, ":")
            for i in range(x+1, y+1, 2):
                print(i)
    elif choice == "S":
        print("Squares from", x, "to", y, ":")
        for i in range (x, y+1):
            print(i*i)
    else:
        print("Invalid choice")
    print("\nMenu:"
          "\n(E)ven numbers from", x, "to", y,
          "\n(O)dd numbers from", x, "to", y,
          "\n(S)quares from", x, "to", y,
          "\n(Q)uit the program")
    choice = input(">>> ")
    choice = choice.upper()
print("\nFinished.")