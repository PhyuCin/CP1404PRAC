class Guitars:
    def __init__(self, name="", year=0, cost=0, age=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = age

    def get_age(self):
        age = 2017 - self.year
        return age

    def is_vintage(self):
        return self.age >= 50

    def __str__(self):
        return "{} ({}): ${}".format(self.name, self.year, self.cost)
