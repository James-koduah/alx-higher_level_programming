#!/usr/bin/python3

"""A rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the class Rectangle
            Args: width, height, x-offset, y-offset
        """
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
        """Returns the area of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Displays what the rectangle would look like
            self.y: offsets the rectangle on the y-axis downwards
            self.x: offsets the rectangle on the x-axis rightwards
        """
        w = self.width
        h = self.height
        for a in range(0, self.y):
            print("")
        for b in range(0, h):
            for c in range(0, self.x):
                print(" ", end="")
            for j in range(0, w):
                print("#", end="")
            print("")

    def to_dictionary(self):
        """You need to write more documentation for this function
            Return: something
        """
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': 10}

    def __str__(self):
        """You need to write more documentation for this function"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """You need to write more documentation for this function
            Return: something
        """
        try:
            self.id = args[0]
        except Exception:
            pass
        try:
            self.__width = args[1]
        except Exception:
            pass
        try:
            self.__height = args[2]
        except Exception:
            pass
        try:
            self.__x = args[3]
        except Exception:
            pass
        try:
            self.__y = args[4]
        except Exception:
            pass

        if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

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
        """You need to write more documentation for this function
            Return: something
        """
        return self.__x

    @x.setter
    def x(self, value):
        """You need to write more documentation for this function
            Return: something
        """
        self.is_an_integer("x", value)
        self.__x = self.is_less_than_zero("x", value)

    @property
    def y(self):
        """You need to write more documentation for this function
            Return: something
        """
        return self.__y

    @y.setter
    def y(self, value):
        """You need to write more documentation for this function
            Return: something
        """
        self.is_an_integer("y", value)
        self.__y = self.is_less_than_zero("y", value)

    @property
    def height(self):
        """You need to write more documentation for this function
            Return: something
        """
        return self.__height

    @height.setter
    def height(self, value):
        """You need to write more documentation for this function
            Return: something
        """
        self.is_an_integer("height", value)
        self.__height = self.is_less_than_zero("height", value, True)

    @property
    def width(self):
        """You need to write more documentation for this function
            Return: something
        """
        return self.__width

    @width.setter
    def width(self, value):
        """You need to write more documentation for this function
            Return: something
        """
        self.is_an_integer("width", value)
        self.__width = self.is_less_than_zero("width", value, True)
