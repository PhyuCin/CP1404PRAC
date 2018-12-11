"""get the fuel and distance to test out the Car class"""

from Prac_06.cars import Car


def main():
    my_car = Car(180, "ferrari")
    my_car.drive(30)

    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print()

    limo = Car(100, "limo")
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)
    print(limo)


main()
