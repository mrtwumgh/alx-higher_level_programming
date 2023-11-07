#!/usr/bin/python3
"""
A module for a square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class for a Square
    """

    def __init__(self, size):
        """
        initializes a square
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """
        returns an area of a square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        returns the string representation of square
        """
        result = "[{}] ".format(str(self.__class__.__name__))
        result += "{}/{}".format(str(self.__size), str(self.__size))
        return result
