#!/usr/bin/python3
"""
A module that defines an area
"""


class BaseGeometry:
    """
    A class that defines an area
    """
    def area(self):
        """
        raises an exception with the message
        area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validates a value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
