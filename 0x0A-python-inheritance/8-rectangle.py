#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
A module that defines classes
"""


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
