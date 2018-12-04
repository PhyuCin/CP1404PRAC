"""Asks the user for a string and then print the counts of how many of each word are in the file.
(Plus formatting)
"""

def main():
    words_to_count = {}
    string = input("Text: ")
    words = string.split()
    words_list = []

    for i in range(len(words)):
        count = words.count(words[i])
        words_to_count[words[i]] = count

    for word in words_to_count.keys():
        words_list.append(word)
    words_list.sort()

    spaces = 0
    for word in words_list:
        if len(word) > spaces:
            spaces = len(word)

    for i in range(len(words_list)):
        print("{:{}} : {}".format(words_list[i], spaces, words_to_count[words_list[i]]))


main()
