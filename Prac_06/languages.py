from Prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)

    programmes = [ruby, python, visual_basic]

    print("\nThe dynamically typed languages are: ")
    for programme in programmes:
        if programme.is_dynamic() is True:
            print(programme.name)


main()


