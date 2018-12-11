from Prac_06.cars import Car
INITIAL_FUEL = 100
INITIAL_ODO = 0


def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    name = Car(INITIAL_FUEL, name)
    name.drive(20)
    print(name.fuel)
    print(name.odometer)


#     my_car = Car(180, "ferrari")
#     my_car.drive(30)
#
#     print("fuel =", my_car.fuel)
#     print("odo =", my_car.odometer)
#     print(my_car)
#     print()
#
#     limo = Car(100, "limo")
#     limo.add_fuel(20)
#     print("fuel =", limo.fuel)
#     limo.drive(115)
#     print("odo =", limo.odometer)
#     print(limo)


main()
