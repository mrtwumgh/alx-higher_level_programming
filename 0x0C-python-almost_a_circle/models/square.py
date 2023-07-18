#!/usr/bin/python3
"""
A module for the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        string representation
        """
        s1 = f"[{self.__class__.__name__}] ({self.id})"
        s2 = f" {self.x}/{self.y} - {self.width}"
        output = s1 + s2
        return output

    @property
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns atributes
        """
        if len(args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
