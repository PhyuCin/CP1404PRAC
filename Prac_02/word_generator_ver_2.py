import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

print("""For word format combinations, you can choose to combine characters with:
(#) - Vowels
(%) - Consonants
(*) - Either vowels or consonants
e.g: as%r#*
""")

word_format = input("Enter the word format: ")
word_format = word_format.lower()

word = ""
for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(VOWELS + CONSONANTS)
    else:
        word += kind

print(word)
