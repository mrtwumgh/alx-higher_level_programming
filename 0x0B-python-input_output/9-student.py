#!/usr/bin/python3
"""
A module for a student class
"""
import json


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

    def to_json(self):
        """
        method that retrieves a dictionary representation
        of a student instance
        """
        return self.__dict__
