"""
A menu will be displayed for the user to choose (quit, choose taxi, drive).
User choose the type of taxi they want, then drive the distance they want to.
The taxi fare for the trip as well as the bill to date will then be displayed.
This repeats until the user quits.
The total tip cost and the taxis are then displayed.
"""

from Prac_08.taxi import Taxi
from Prac_08.silverservicetaxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive\n>>>"

"""0 - Prius, fuel=100, odo=0, 0km on current fare, $1.20/km
1 - Limo, fuel=100, odo=0, 0km on current fare, $2.40/km plus flagfall of $4.50
2 - Hummer, fuel=200, odo=0, 0km on current fare, $4.80/km plus flagfall of $4.5"""


def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0.0
    taxi = 0
    menu_choice = input(MENU).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            for i in range(len(taxis)):
                print(i, "-", taxis[i])
            taxi = int(input("Choose taxi: "))
        elif menu_choice == "d":
            distance = int(input("Drive how far?"))
            taxis[taxi].drive(distance)
            fare = taxis[taxi].get_fare()
            bill_to_date += fare
            print("Your {} trip cost you ${:.2f}".format(taxis[taxi].name, fare))
            taxis[taxi].start_fare()
        else:
            print("Invalid menu choice!")
        print("Bill to date: ${0:.2f}".format(bill_to_date))
        menu_choice = input(MENU).lower()

    print("Total trip cost: ${:.2f}".format(bill_to_date))
    print("Taxis are now:")
    for i in range(len(taxis)):
        print(i, "-", taxis[i])


main()
