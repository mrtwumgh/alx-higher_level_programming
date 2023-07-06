#!/usr/bin/python3
"""
A module that defines a square
"""


class Square:
    """
    A class that defines a square

    Args:
        size: size of the square
    Attributes:
        size: size of the square

    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns the area of the square
        """
        return self.__size * self.__size
