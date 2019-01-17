import wikipedia


def main():
    search_phrase = input("Enter a search phrase: ")
    if wikipedia.suggest(search_phrase) is None:
        print(", ".join(wikipedia.search(search_phrase)))
    else:
        print(wikipedia.suggest(search_phrase))


main()
