from Prac_08.unreliable_car import UnreliableCar


def main():
    ucar1 = UnreliableCar("Black", 100, 50)

    ucar1.drive(40)
    print(ucar1)

    ucar1.drive(100)
    print(ucar1)


main()
