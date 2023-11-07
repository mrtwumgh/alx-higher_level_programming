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
