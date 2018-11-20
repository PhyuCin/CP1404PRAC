"""Input a name and print alternate character"""


def main():
    name = get_name()
    num = input("Enter the step: ")
    num = check_integer(num)
    num = check_stepnum(num)
    print(name[::num])


def check_stepnum(num, name):
    while num == 0 or num > len(name):
        print("Invalid step")
        num = input("Enter the step: ")
        num = check_integer(num)
    return num


def check_integer(num):
    while not num.isdigit():
        try:
            num = int(input("Enter the step: "))
        except ValueError:
            print("Invalid step")
            num = input("Enter the step: ")
    return num


def get_name():
    name = input("Enter name: ")
    while len(name) <= 1:
        print("Invalid")
        name = input("Enter long name: ")
    return name


main()