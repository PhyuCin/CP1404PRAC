from Prac_06.guitars_class import Guitars

def main():
    print("My guitars!")
    guitars = []
    more_songs = True
    while more_songs is True:
        name = input("Name: ")
        if name != "":
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            guitar = Guitars(name, year, cost)
            print(guitar, "added.")
            guitars.append(guitar)
        else:
            more_songs = False
    for i in range(len(guitars)):
        guitars[i].age = guitars[i].get_age()
        if guitars[i].is_vintage() is True:
            print("Guitar {}: {:>20} ({}), worth ${:>10} (vintage)".format(i + 1, guitars[i].name, guitars[i].year,
                                                                           guitars[i].cost))

        else:
            print("Guitar {}: {:>20} ({}), worth ${:>8}".format(i+1, guitars[i].name, guitars[i].year,
                                                                 guitars[i].cost))


main()
