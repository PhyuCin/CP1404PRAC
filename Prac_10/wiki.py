import wikipedia


def main():
    search_phrase = "Empty"
    while search_phrase != "":
        print("Enter a search phrase (or enter a blank to exit)")
        search_phrase = input(">>> ")
        if search_phrase == "":
            continue
        elif wikipedia.suggest(search_phrase) is None:
            print(wikipedia.summary(search_phrase))
        else:
            print("Suggestion:", wikipedia.suggest(search_phrase))
    print("Bye~")


main()
