#!/usr/bin/python3

""" A simple function that reads a file and prints to stdout"""


def read_file(filename=""):
    """Returns contents of file to stdout"""

    with open(filename, encoding="utf-8") as a_file:
        for line in a_file:
            print(line)

