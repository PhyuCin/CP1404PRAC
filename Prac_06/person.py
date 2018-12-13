from Prac_06.people import People
import operator


TABLE_LINE = "-"*36


def main():
    person_list = []
    print("How many people?")
    number = int(input(">>> "))
    for i in range(number):
        print("Person", i+1)
        first_name = input("First name: ").title()
        last_name = input("Last name: ").title()
        age = int(input("Age: "))

        person = People(first_name, last_name, age)
        person_list.append(person)

    print()
    person_list.sort(key=operator.attrgetter('age'))

    print("{:18} {:13} {:5}".format("First Name", "Last Name", "Age"))
    for i in range(len(person_list)):
        print(TABLE_LINE)
        print(person_list[i])
    print(TABLE_LINE)


main()
