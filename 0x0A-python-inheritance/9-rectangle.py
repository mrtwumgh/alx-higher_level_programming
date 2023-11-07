#!/usr/bin/python3
"""A module for a rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class of a rectangle
    """

    def __init__(self, width, height):
        """
        initializes a rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns the string representation of rectangle
        """
        result = "[{}] ".format(str(self.__class__.__name__))
        result += "{}/{}".format(str(self.__width), str(self.__height))
        return result
