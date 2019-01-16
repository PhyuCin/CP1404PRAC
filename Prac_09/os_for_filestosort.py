"""
CP1404/CP5632 Practical
"""
import shutil
import os

def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    extensions = []

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename.split(".", 1)[1]
        if extension not in extensions:
            os.mkdir(extension)
            extensions.append(extension)
        shutil.move(filename, extension + "/" + filename)
        print("Moved {} to {}".format(filename, extension))


main()

