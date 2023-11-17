#!/usr/bin/python3
"""
A module that tests the rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
    tests for the class Rectangle
    """

    def setUp(self):
        """
        set up of objects
        """
        self.r1 = Rectangle(10, 2, 0, 0, 12)
        self.r2 = Rectangle(3, 7, 1, 1)
        self.r3 = Rectangle(8, 5, 2, 4)

    def test_attributes(self):
        """
        test case for checking values
        """
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

    def test_id_inheritance(self):
        """
        test case for checking id
        """
        self.assertEqual(self.r1.id, 12)
        self.assertEqual(self.r2.id, 5)

    def test_setters(self):
        """
        test for setters
        """
        self.r2.width = 7
        self.r2.height = 9
        self.r2.x = 3
        self.r2.y = 5

        self.assertEqual(self.r2.width, 7)
        self.assertEqual(self.r2.height, 9)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r2.y, 5)

    def test_invalid_values(self):
        """
        tests invalud values for setters
        """
        with self.assertRaises(TypeError):
            self.r1.width = "invalid_integer"
        with self.assertRaises(ValueError):
            self.r1.width = 0
        with self.assertRaises(TypeError):
            self.r1.height = "invalid_integer"
        with self.assertRaises(ValueError):
            self.r1.height = 0
        with self.assertRaises(TypeError):
            self.r1.x = "invalid_integer"
        with self.assertRaises(ValueError):
            self.r1.x = -2
        with self.assertRaises(TypeError):
            self.r1.y = "invalid_integer"
        with self.assertRaises(ValueError):
            self.r1.y = -3

    def test_area(self):
        """
        tests the area method
        """
        self.assertEqual(self.r2.area(), 21)
        self.assertEqual(self.r3.area(), 40)

    def tearDown(self):
        """
        teardown of instances
        """
        del self.r1
        del self.r2


if __name__ == "__main__":
    unittest.main()
