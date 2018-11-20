import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = input("Enter the word format using 'c' for consonants and 'v' for vowels: ")
word_format = word_format.lower()
allowed = set('c' + 'v')

while set(word_format) != allowed:
    print("Invalid word format")
    word_format = input("Enter the word format using 'c' for consonants and 'v' for vowels: ")
    word_format = word_format.lower()

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)
