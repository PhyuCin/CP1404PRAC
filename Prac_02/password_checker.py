SPECIAL = "!@#$%^&*()_-=+`~,./'[]<>?{}|\ "
MIN = 5
MAX = 15

print("""Please enter a valid password
Your password must be between 5 and 15 characters, and contain:
    1 or more uppercase characters
    1 or more lowercase characters
    1 or more numbers
    and 1 or more special characters:  !@#$%^&*()_-=+`~,./'[]<>?{}|\\
""")

password = input("> ")
lower = 0
upper = 0
number = 0
special = 0

check = "invalid"
while check == "invalid":
    while len(password) < 5 or len(password) > 15:
        print("Invalid password!")
        password = input("> ")
    for character in password:
        if character.islower():
            lower += 1
        elif character.isupper():
            upper += 1
        elif character.isdigit():
            number += 1
        elif character in SPECIAL:
            special += 1
    if lower == 0:
        check = "invalid"
        print("Invalid password!")
        password = input("> ")
    elif upper == 0:
        check = "invalid"
        print("Invalid password!")
        password = input("> ")
    elif number == 0:
        check = "invalid"
        print("Invalid password!")
        password = input("> ")
    elif special == 0:
        check = "invalid"
        print("Invalid password!")
        password = input("> ")
    else:
        check = "valid"

print("\nYour {} character password is valid: {}".format(len(password), password))
