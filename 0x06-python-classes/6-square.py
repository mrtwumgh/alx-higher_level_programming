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

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("Position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """
        getter for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter for position
        """
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("Position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        returns the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints out the square
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
