#!/usr/bin/python3
"""A Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass of the rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.is_an_integer("width", value)
        self.__width = self.is_less_than_zero("width", value, True)
        self.__height = self.is_less_than_zero("width", value, True)

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

    def update(self, *args, **kwargs):
        """ This is a way of updating values in the Square class
            *args: The first value is for the id
                    The second value is for the size
            (Note that both height and width of the square have the same value)
                    The third value is for the x offset
                    The fourth value is for the y offset
            *kwargs: Special key:value pairs that specify which value to update
        """
        try:
            self.id = args[0]
        except Exception:
            pass
        try:
            self.width = args[1]
        except Exception:
            pass
        try:
            self.height = args[1]
        except Exception:
            pass
        try:
            self.x = args[2]
        except Exception:
            pass
        try:
            self.y = args[3]
        except Exception:
            pass

        if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
