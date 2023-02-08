#!/usr/bin/python3
"""Checks to see if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """Checks to see if 
        obj inherits directly ofr indirectly from a_class
        Return True or False
    """
    if issubclass(type(obj), a_class) is True and type(obj) != a_class:
        return True
    return False
