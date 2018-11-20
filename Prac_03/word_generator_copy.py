import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():

    word_format = input("Enter the word format using 'c' for consonants and 'v' for vowels: ")
    word_format = word_format.lower()

    while is_valid_format(word_format) is False:
        print("Invalid word format")
        word_format = input("Enter the word format using 'c' for consonants and 'v' for vowels: ")
        word_format = word_format.lower()
        valid = is_valid_format(word_format)

    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)


def is_valid_format(word_format):
    for char in word_format:
        if char != "c":
            if char != "v":
                return False
    return True


main()