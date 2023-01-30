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

    @property
    def size(self):
        """Return private variable"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set private variable"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
