#!/usr/bin/python3
"""
A module for a class square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class for a square
    """
    def __init__(self, size):
        """
        Initializes a square
        Args:
            size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
