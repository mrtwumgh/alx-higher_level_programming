#!/usr/bin/python3
"""Defines the class: Square"""


class Square:
    """
    A class that represents a square

    Attributes:
        __size(int): The size of the square(default:0)
    """
    def __init__(self, size=0):
        """
        Initializes the attributes of square

        Args:
           - size(int): The size of the square

        Raises:
           - TypeError: size muse be an integer
           - ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: area of the square
        """
        return self.__size ** 2
