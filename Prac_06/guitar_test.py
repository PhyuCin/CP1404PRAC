from Prac_06.guitars_class import Guitars

gibson_l_5_ces = Guitars("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitars("Another Guitar", 2012)

print(gibson_l_5_ces)

gibson_l_5_ces.age = gibson_l_5_ces.get_age()

print(gibson_l_5_ces.age)
print(gibson_l_5_ces.is_vintage())

another_guitar.age = another_guitar.get_age()
print(another_guitar.age)
print(another_guitar.is_vintage())