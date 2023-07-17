#!/usr/bin/python3
"""
tests for the class rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


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
            with self.assertRaisesRegex(TypeError, "x must be an intger"):
                r.x = "not an int"
            with self.assertRaisees(VaueError):
                r.y = -1

if __name__ == "__main__":
    unittest.main()
