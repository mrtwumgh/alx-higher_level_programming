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
        self.size = size
        self.x = x
        self.y = y
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
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        updates attribute values
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = kwargs[key]
                if key == "size":
                    self.size = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]
