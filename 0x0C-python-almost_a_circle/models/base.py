#!/usr/bin/python3
"""
A module for the class Base
"""


class Base:
    """
    A class to serve as the Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
