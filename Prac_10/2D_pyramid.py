def get_row():
    row = int(input("Enter number of rows for the pyramid: "))
    print("Total number of blocks:", pyramid(row))


def pyramid(n):
    """Create pyramid based on the number of rows the user gives it."""
    if n <= 0:
        return 0
    return n + pyramid(n - 1)


get_row()
