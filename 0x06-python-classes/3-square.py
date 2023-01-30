#!/usr/bin/python3
"""A Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Instance of Square

        Args:
            size (int): size of square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)
