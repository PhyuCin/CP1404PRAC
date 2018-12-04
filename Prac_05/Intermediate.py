"""Return hex colour code when a colour name is entered"""

COLOUR_NAMES = {'white': '#ffffff', 'black': '#000000', 'red': '#ff0000', 'blue': '#4876ff', 'yellow': '#ffff00',
                'orange': '#ff7f00', 'green': '#00ee76', 'skyblue': '#87ceff', 'purple': '#b452cd', 'pink': '#ffb5c5'}


def main():
    valid = False
    colour_name = ""
    while valid is False:
        colour_name = input("Enter colour name: ").lower()
        valid = check(colour_name)
    print("Code:", COLOUR_NAMES[colour_name])


def check(colour_name):
    for name, code in COLOUR_NAMES.items():
        if name == colour_name:
            return True
    print("Invalid choice!\n")
    return False


main()