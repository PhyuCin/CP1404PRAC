LOWER = 33
UPPER =127

def main():

    character_input = input("Enter a character: ")
    code = ord(character_input)
    print("The ASCII code for {} is {}".format(character_input, code))

    code_input = get_number()

    character = chr(code_input)
    print("The character for {} is {}".format(code_input, character))

    #column_num = int(input("Enter number of columns: "))
    #while column_num < 1 or column_num > 127:
        #print("Invalid column number")
        #column_num = int(input("Enter number of columns: "))

    for i in range (33, 128):
        print("{} {}".format(i,chr(i)))


def get_number():
    valid = False
    while valid is False:
        code_input = input("Enter a number between {} and {}: ".format(LOWER, UPPER))
        try:
            code_input = int(code_input)
            valid = True
            if code_input < LOWER or code_input > UPPER:
                print("Invalid number!")
                valid = False
        except ValueError:
            print("Invalid number!")
            valid = False
    return code_input


main()