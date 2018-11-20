import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

print("""For word format:
(C)onsonants and 'v' for vowels:""")
word_format = input("Enter the word format using 'c' for consonants and 'v' for vowels: ")
word_format = word_format.lower()

if word_format == "auto":
    word_format = ""
    word_num = random.randrange(2,13)
    for num in range (0, word_num):
        word_format += random.choice("c" + "v")
    print("Word format:", word_format)

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)
