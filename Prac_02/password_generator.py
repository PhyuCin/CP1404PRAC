import random

LOWER_CHAR = "abcdefghijklmnopqrstuvwxyz"
UPPER_CHAR = LOWER_CHAR.upper()
NUM = "0123456789"
SPECIAL = "!@#$%^&*()_-=+`~,./'[]<>?{}|\ "


print("Password Generator\n")

length = int(input("Enter the password length: "))

menu = """
Characteristics:
(A) 1 or more uppercase characters
(B) 1 or more lowercase characters 
(C) 1 or more numbers 
(D) 1 or more special characters

Choose one or more characteristics for the password
e.g. ACD
"""

choice_a = "(A) 1 or more uppercase characters"
choice_b = "(B) 1 or more lowercase characters "
choice_c = "(C) 1 or more numbers "
choice_d = "(D) 1 or more special characters"

print(menu)
characteristics = input(">>> ")
characteristics = characteristics.lower()
allowed = set("abcd")

while not set(characteristics).issubset(allowed):
    print("Invalid choices")
    print(menu)
    characteristics = input(">>> ")
    characteristics = characteristics.lower()


while length < len(characteristics):
    print("\nYour password length cannot be less than the number of characteristics you choose.")
    length = int(input("Enter the password length: "))
    print(menu)
    characteristics = input(">>> ")
    characteristics = characteristics.lower()
    allowed = set("abcd")

    while not set(characteristics).issubset(allowed):
        print("Invalid choices")
        print(menu)
        characteristics = input(">>> ")
        characteristics = characteristics.lower()


password = ""

if "a" in characteristics:
    password += random.choice(UPPER_CHAR)
if "b" in characteristics:
    password += random.choice(LOWER_CHAR)
if "c" in characteristics:
    password += random.choice(NUM)
if "d" in characteristics:
    password += random.choice(SPECIAL)

for i in range(0, length - len(characteristics)):
    password += random.choice(UPPER_CHAR + LOWER_CHAR + NUM + SPECIAL)

password_var = list(password)
random.shuffle(password_var)

print("Your password length is", length, "and its characteristics are:")
for kind in characteristics:
    if kind == "a":
        print(choice_a)
    elif kind == "b":
        print(choice_b)
    elif kind == "c":
        print(choice_c)
    else:
        print(choice_d)

print("\nPassword:")
print(''.join(password_var))

