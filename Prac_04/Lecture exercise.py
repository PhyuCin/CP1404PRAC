"""Group 5"""

VOWELS = "aeiouAEIOU"

name = input("Enter your name: ")
vowel = 0
for char in name:
    if char in VOWELS:
        vowel += 1
print("Name:", name)
print("Out of {} letters, {} has {} vowels.".format(len(name), name, vowel))

