#!/usr/bin/python3

"""Addition function"""


def add_integer(a, b=98):
    """Returns sum of a and b

    Raises:
        TypeError: if arguments are not int or floats
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
