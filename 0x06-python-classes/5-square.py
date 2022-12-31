#!/usr/bin/python3
"""Defines the class: Square"""


class Square:
    """
    A class that represents a square

    Attributes:
        size(int): the size of the square
    """
    def __init__(self, size=0):
        """
        Initialize the attributes of the square

        Args:
            - __size(int): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        Return the size of the square.

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
            - size: The size of the square

        Raises:
            - TypeError: size must be an integer
            - ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
