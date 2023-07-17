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
