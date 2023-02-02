#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        b = self.width + self.height
        return (2 * b)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")

        jj = []
        for i in range(0, self.height):
            for x in range(0, self.width):
                jj.append(str(self.print_symbol))
            if i == self.height - 1:
                break
            jj.append("\n")
        return ("".join(jj))

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")

        a = rect_1.area()
        b = rect_2.area()
        if a > b:
            return rect_1
        elif b > a:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
