#!/usr/bin/python3
"""
A module that represents a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class that represents a square
    """

    def __init__(self, size, x = 0, y = 0, id = None):
        """
        Initializes the attributes
        """
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
