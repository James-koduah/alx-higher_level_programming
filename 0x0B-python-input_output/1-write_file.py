#!/usr/bin/python3

"""Write to a file (Overwrite)"""


def write_file(filename="", text=""):
    """OverWrite the string in text to the variable ``filename``
    Creat a new file if none exists
    """
    b = 0
    with open(filename, mode='w', encoding='utf-8') as a_file:
        b = a_file.write(text)

    return b
