from Prac_08.silverservicetaxi import SilverServiceTaxi


def main():
    silvertaxi = SilverServiceTaxi("SST1", 200, 2)
    print(silvertaxi)

    silvertaxi.drive(18)
    print(silvertaxi)
    print("The current fare is {:.2f}".format(silvertaxi.get_fare()))
    silvertaxi.start_fare()

    # silvertaxi.drive(100)
    # print(silvertaxi)
    # print("The current fare is ${}".format(silvertaxi.get_fare()))


main()
