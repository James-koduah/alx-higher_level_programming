#!/usr/bin/python3
"""Inherit from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""

    def __init__(self, width, height):
        """Initialization function"""
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height
