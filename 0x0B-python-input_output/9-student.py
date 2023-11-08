#!/usr/bin/python3
"""
A module of a class student
"""


class Student:
    """
    A class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        initializes a new instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """
        retrieves a dictionary representation of Student
        """
        return self.__dict__
