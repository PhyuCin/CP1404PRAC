def main():
    strings = []
    repeats = []
    print("Enter your strings, one at a time. Enter empty string when done.")
    string = "empty"
    while string != "":
        string = input("Enter a string: ")
        if string != "":
            strings.append(string)

    for i in range(len(strings)):
        if strings.count(strings[i]) > 1:
            repeats.append(strings[i])
    if repeats == []:
        print("No repeated strings entered")
    else:
        repeats = list(dict.fromkeys(repeats))
        print("Strings repeated:", ', '.join(repeats))


main()