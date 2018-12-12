from Prac_06.cars import Car
MENU = """Menu:
d) drive
r) refuel
q) quit"""


def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    name = Car(100, name)
    print(name)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while not choice == "q":
        if choice == "d":
            distance = int(input("How many km do you wish to drive? "))
            while distance <= 0:
                print("Distance must be >= 0")
                distance = int(input("How many km do you wish to drive? "))
            if distance <= name.fuel:
                name.drive(distance)
                print("The car drove {}km.".format(distance))
            else:
                print("The car drove {}km and ran out of fuel.".format(name.fuel))
                name.drive(distance)

        elif choice == "r":
            fuel_amount = int(input("How many units of fuel do you want to add to the car? "))
            while fuel_amount <= 0:
                print("Fuel amount must be >= 0")
                fuel_amount = int(input("How many units of fuel do you want to add to the car? "))
            name.add_fuel(fuel_amount)
            print("Added {} units of fuel.".format(fuel_amount))

        else:
            print("Invalid choice")
        print()
        print(name)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print("\nGood bye {}'s driver.".format(name.name))


main()
