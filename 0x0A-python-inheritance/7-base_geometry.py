#!/usr/bin/python3
"""
A module for an empty BaseGeometry class
"""


class BaseGeometry:
    """
    A BaseGeometry class
    """
    def area(self):
        """
        a method not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        a method that validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
