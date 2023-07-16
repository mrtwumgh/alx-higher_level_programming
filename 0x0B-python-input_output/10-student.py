#!/usr/bin/python3
"""
A module for a student class
"""


class Student:
    """
    A class that defines a student

    Attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method that retrieves a dictionary representation
        of a student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for key in attrs:
                if hasattr(self, key):
                    result[key] = getattr(self, key)

            return result
