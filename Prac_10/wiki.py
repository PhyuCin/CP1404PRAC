import wikipedia


def main():
    search_phrase = "Empty"
    while search_phrase != "":
        print("Enter a search phrase (or enter a blank to exit)")
        search_phrase = input(">>> ")
        if search_phrase == "":
            continue
        elif wikipedia.suggest(search_phrase) is None:
            try:
                page = wikipedia.page(search_phrase)
                title = page.title
                summary = wikipedia.summary(search_phrase)
                url = page.url
                print(title)
                print(summary)
                print(url)
            except wikipedia.exceptions.DisambiguationError as e:
                print("Suggestions:\n" + ", ".join(e.options))
            except wikipedia.exceptions.PageError:
                print("The page", search_phrase, "does not exist")
        else:
            print("Suggestion:", wikipedia.suggest(search_phrase))
    print("Bye~")


main()
