#!/usr/bin/python3
"""Empyt class"""


class BaseGeometry():
    """Nothing"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates argument value
            If ```value``` is not an integer 
                raise error
            if ```value``` is less than 1
                raise error
            Returns nothing
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value < 1:
            raise ValueError(f"{name} must be greater than 0")
