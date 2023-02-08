#!/usr/bin/python3
"""Checks if class is an instance of anothe class"""


def is_kind_of_class(obj, a_class):
    """Checks if 
        obj is an instance of a subclass of a_class
        Returns True if obj is an instance of a_class else reutrn false
    """
    if isinstance(obj, a_class) == True:
        return True
    return False
