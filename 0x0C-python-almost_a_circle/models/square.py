#!/usr/bin/python3
"""
A module that represents a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class that represents a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the attributes
        """
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """
        returns the size
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        sets the value for size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            self.__width = value
            self.__height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
