#!/usr/bin/python3
"""
A module that defines classes
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that defines a rectangle
    """
    def __init__(self, width, height):
        """
        Initializes the rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns the string representation
        """
        s = f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
        return s
