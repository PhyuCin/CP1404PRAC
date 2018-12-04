"""Takes the birth dates and return the ages of the people in the list"""

from datetime import date

names = ["Jack", "Jill", "Joe", "Jin", "James"]
today = date.today()
name_to_age = {}

for i in range(len(names)):
    date_of_birth = input("Enter {}'s date of birth (DD/MM/YYYY): ".format(names[i]))
    born_day, born_month, born_year = date_of_birth.strip().split("/")
    age = today.year - int(born_year) - ((today.month, today.day) < (int(born_month), int(born_day)))
    name_to_age[names[i]] = age

for i in range(len(names)):
    print("{}. Name: {}".format(i+1, names[i]))
    print("   Age:", name_to_age[names[i]])
    print()

