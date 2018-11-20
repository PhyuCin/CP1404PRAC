"""Input a name and print alternate character"""


def main():
    name = get_name()
    num = get_step(name)
    print(name[::num])


def get_step(name):
    num = input("Enter the step: ")
    num = check_integer(num)
    while num == 0 or num > len(name):
        print("Invalid step")
        num = input("Enter the step: ")
        num = check_integer(num)
    return num


def check_integer(num):
    while not num.isdigit():
        print("Invalid step")
        num = input("Enter the step: ")
    num = int(num)
    return num


def get_name():
    name = input("Enter name: ")
    while len(name) <= 1:
        print("Invalid")
        name = input("Enter long name: ")
    return name


main()