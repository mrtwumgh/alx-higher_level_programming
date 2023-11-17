#!/usr/bin/python3
"""
A module for a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    A class that defines a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an instance of Rectangle
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """
        returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        returns the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the value of x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        returns the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the value of y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints the rectangle using #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        returns the string representation of the rectangle
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args):
        """
        assigns an argument to each attribute
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.__width = args[1]
            if i == 2:
                self.__height = args[2]
            if i == 3:
                self.__x = args[3]
            if i == 4:
                self.__y = args[4]
