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

        r1 = Rectangle(4, 3, 2, 1)
        output = StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__
        expected = "\n  ####\n  ####\n  ####\n"
        self.assertEqual(output.getvalue(), expected)

    def test_with_x_y(self):
        """
        test the printout with x and y specified
        """
        r = Rectangle(2, 3, 2, 2)
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
        """
        tests the magic method __str__
        """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (5) 3/4 - 1/2')

    def test_update_args(self):
        """
        test *args
        """
        r = Rectangle(1, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_update_kwargs(self):
        """
        test **kwargs
        """
        r = Rectangle(1, 1)
        r.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_update_args_and_kwargs(self):
        """
        test both args and kwargs
        """
        r = Rectangle(1, 1)
        r.update(2, 3, height=4, x=5, y=6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9)
        dic = r.to_dictionary()
        self.assertEqual(dic, {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

        r = Rectangle(1, 1)
        dic = r.to_dictionary()
        self.assertEqual(dic, {'id': 6, 'width': 1, 'height': 1, 'x': 0, 'y': 0})

if __name__ == "__main__":
    unittest.main()
