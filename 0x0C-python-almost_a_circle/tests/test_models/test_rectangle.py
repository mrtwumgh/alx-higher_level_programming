#!/usr/bin/python3
"""
tests for the class rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangleClass(unittest.TestCase):
    """
    test methods
    """
    def test_initialization(self):
        """
        tests initialization
        """
        r = Rectangle(5, 10, 20, 45, 39)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 45)
        self.assertEqual(r.id, 39)

    def test_width(self):
        """
        tests width
        """
        r = Rectangle(20, 30)
        self.assertEqual(r.width, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "not an int"
        with self.assertRaises(ValueError):
            r.width = -1

    def test_height(self):
        """
        tests height
        """
        r = Rectangle(36, 96)
        self.assertEqual(r.height, 96)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = "not an int"
        with self.assertRaises(ValueError):
            r.height = -2

    def test_x(self):
        """
        tests x
        """
        r = Rectangle(12, 34)
        self.assertEqual(r.x, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = "not an int"
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        """
        tests the return value of area
        """
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """
        tests the printout of rectangle
        """
        r = Rectangle(4, 3)
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "####\n####\n####\n")

    def test_with_x_y(self):
        """
        test the printout with x and y specified
        """
        r = Rectangle(2, 3, 2, 2)
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n##\n")

if __name__ == "__main__":
    unittest.main()
