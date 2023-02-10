#!/usr/bin/python3

"""A rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.is_an_integer("width", width)
        self.is_an_integer("height", height)
        self.is_an_integer("x", x)
        self.is_an_integer("y", y)

        self.__width = self.is_less_than_zero("width", width, True)
        self.__height = self.is_less_than_zero("height", height, True)
        self.__x = self.is_less_than_zero("x", x)
        self.__y = self.is_less_than_zero("y", y)

    def area(self):
        return self.width * self.height

    def is_an_integer(self, name, value):
        """A custom function not part of the ALX guide

            Returns an error if value is less than zero
            else returns True
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

    def is_less_than_zero(self, name, value, less_equal=False):
        """ Checks if value < zero or if value <= zero
            if less_equal == False
                we check if value < zero
            else if less_equal == True
                we check if value <= zero
        """
        if less_equal is False:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
            else:
                return value
        else:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
            else:
                return value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.is_an_integer("x", value)
        self.__x = self.is_less_than_zero("x", value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.is_an_integer("y", value)
        self.__y = self.is_less_than_zero("y", value)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.is_an_integer("height", value)
        self.__height = self.is_less_than_zero("height", value, True)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.is_an_integer("width", value)
        self.__width = self.is_less_than_zero("width", value, True)
