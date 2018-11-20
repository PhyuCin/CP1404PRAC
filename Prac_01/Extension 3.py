username = input("Enter name: ")

menu = """(H)ello
(G)oodbye
(Q)uit"""

print(menu)

choice = input(">>> ")
choice = choice.upper()

while choice != "Q":
    if choice == "H":
        print("Hello", username)
    elif choice == "G":
        print ("Goodbye", username)
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>> ")
    choice = choice.upper()

print("Finished.")
