#!/usr/bin/python3

"""Append to a file"""


def append_write(filename="", text=""):
    """OverWrite the string in text to the variable ``filename``
    Creat a new file if none exists
    """
    b = 0
    with open(filename, mode='a', encoding='utf-8') as a_file:
        b = a_file.write(text)

    return b
