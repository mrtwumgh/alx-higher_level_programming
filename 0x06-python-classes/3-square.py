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

    def area(self):
        """
        a function that returns the area
        Returns:
            The return value. The area of the square

        """

        return self.__size * self.__size
