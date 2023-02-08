#!/usr/bin/python3
"""Checks is object is an instance of another"""


def is_same_class(obj, a_class):
    """Checkes if the argument
        obj is an instance of a_class

        Return: True if obj is an instance of a_class else return False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
