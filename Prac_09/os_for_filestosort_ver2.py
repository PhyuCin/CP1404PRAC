"""
CP1404/CP5632 Practical
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort_2')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    ex_doc = input('What category would you like to sort doc files into?')
    ex_docx = input('What category would you like to sort docx files into?')
    ex_png = input('What category would you like to sort png files into?')
    ex_gif = input('What category would you like to sort gif files into?')
    ex_txt = input('What category would you like to sort txt files into?')
    ex_xls = input('What category would you like to sort xls files into?')
    ex_xlsx = input('What category would you like to sort xlsx files into?')
    ex_jpg = input('What category would you like to sort jpg files into?')
    categories = [ex_doc, ex_docx, ex_png, ex_gif, ex_txt, ex_xls, ex_xlsx, ex_jpg]
    for category in categories:
        try:
            os.mkdir(category)
        except FileExistsError:
            pass

    category_dic = {"doc": ex_doc, "docx": ex_docx, "png": ex_png, "gif": ex_gif, "txt": ex_txt,
                    "xls": ex_xls, "xlsx": ex_xlsx, "jpg": ex_jpg}

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue
        extension = filename.split(".", 1)[1]
        category = category_dic.get(extension)
        shutil.move(filename, category + "/" + filename)
        print("Moved {} to {}".format(filename, category))


main()


