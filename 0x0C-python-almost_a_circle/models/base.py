#!/usr/bin/python3

"""Base class for all other classes"""


class Base():
    """The parent class of this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init function"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
