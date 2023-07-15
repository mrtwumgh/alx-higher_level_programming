#!/usr/bin/python3
"""
A module that defines classes
"""


class BaseGeometry:
    """
    A class that defines an area
    """
    def area(self):
        """
        raises an exception with the message
        area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validates a value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class that defines a rectangle
    """
    def __init__(self, width, height):
        """
        Initializes the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
