import random

INITIAL_POPULATION = 1000
WITH_MIN_BORN = 1.1
WITH_MAX_BORN = 1.2
WITH_MIN_DIED = 1.05
WITH_MAX_DIED = 1.25


def main():
    print("Welcome to the Gopher Population Simulator!"
          "\nStarting population:", INITIAL_POPULATION)
    current_population = INITIAL_POPULATION
    for i in range(1, 11):
        born = get_new_born(current_population)
        died = get_new_died(current_population)
        current_population = current_population + born - died
        print("""
Year {}
*****
{} gophers were born. {} died.
Population: {}""".format(i, born, died, current_population))


def get_new_born(current_population):
    born = random.randint((current_population * WITH_MIN_BORN)//1, (current_population * WITH_MAX_BORN - 1)//1)
    return born


def get_new_died(current_population):
    died = random.randint((current_population * WITH_MIN_DIED//1), (current_population * WITH_MAX_DIED - 1)//1)
    return died


main()