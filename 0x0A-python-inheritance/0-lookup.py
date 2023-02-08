#!/usr/bin/python3

"""Produce methods and attributes of an object"""


def lookup(obj):
    """Checks for available methods and attributes
    Return: a list object
    """
    return dir(obj)
