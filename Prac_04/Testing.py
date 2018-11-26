def main():
    character = input("Enter a character: ")
    new_num = ord(character)
    print("The ASCII for ",character,"is ",new_num)
    lower = int(33)
    upper = int(127)
    number = get_number(lower, upper)
    while number < lower or number > upper:
        print("Number must be between 33 and 127")
        number = input("Enter a number between 33 and 127: ")
    new_chr = chr(number)
    print(new_chr)

    for i in range(33, 128):
        ch = chr(i);
        print("{:>4}".format(i),"{:>4}".format(ch))

def get_number(lower, uppper):
    error_check = True
    while error_check == True:
        try:
            number = int(input("Enter a number between 33 and 127: "))
            error_check = False

        except ValueError:
            print("Input must be a number")
            error_check = True

    return number


main()