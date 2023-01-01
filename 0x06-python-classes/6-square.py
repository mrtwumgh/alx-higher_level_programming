#!/usr/bin/python3
"""A module that represents a class"""


class Square:
    """
    A class that represents a square

    Attritbutes:
        - size: defines the square
        - position: defines the position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the size and position attributes

        Args:
            - __size : defines the square
            - __position: defines the position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Returns the size of the square

        Returns:
            - size(int): the size of the square
        """

    @size.setter
    def size(self, value):
        """
        Sets the value of size

        Args:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Returns the position of the square

        Returns:
            - position(tuple): the position of the square
        """

    @position.setter
    def position(self, value):
        """
        sets the value of position

        Args:
            value: the value to be set
        """
        if not (
            isinstance(value, tuple)
            and len(value) != 2
            and all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square

        Returns:
            - area: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints to stdout the square with the character '#'
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print("")
