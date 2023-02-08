#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    """MyList is a subclass of the list class"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        p = sorted(self)
        print(p)
