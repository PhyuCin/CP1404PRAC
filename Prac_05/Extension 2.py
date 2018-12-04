"""Takes 2 lists and creates a dictionary with the elements in one of the list as the key and
the elements in the other as the values"""

names = ["Jack", "Jill", "Harry"]
dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

names_to_dobs = dict(zip(names, dobs))

print(names_to_dobs)