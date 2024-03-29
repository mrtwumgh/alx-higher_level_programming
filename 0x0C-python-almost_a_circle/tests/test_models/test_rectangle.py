#!/usr/bin/python3
"""
A module that tests the rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


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
        self.assertEqual(self.r2.id, 29)

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

    def test_display(self):
        """
        tests the output of the display method
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        self.r2.display()

        sys.stdout = sys.__stdout__
        expected_output = "\n ###\n ###\n ###\n ###\n ###\n ###\n ###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        """
        tests the str method
        """
        self.assertEqual(str(self.r2), "[Rectangle] (35) 1/1 - 3/7")
        self.assertEqual(str(self.r1), "[Rectangle] (12) 0/0 - 10/2")

    def test_update_args(self):
        """
        tests the update method with args
        """
        self.r1.update(10, 3, 4, 2, 1)

        self.assertEqual(self.r1.id, 10)
        self.assertEqual(self.r1.width, 3)
        self.assertEqual(self.r1.height, 4)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 1)

    def test_update_kwargs(self):
        """
        tests the update method with kwargs
        """
        self.r1.update(width = 5, height = 8, y = 6, x = 3)

        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r1.height, 8)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 6)

    def test_to_dictionary(self):
        """
        tests the to_dictionary method
        """
        expected_result = {
                "id": 12,
                "width": 10,
                "height": 2,
                "x": 0,
                "y": 0
        }
        self.assertEqual(self.r1.to_dictionary(), expected_result)

    def tearDown(self):
        """
        teardown of instances
        """
        del self.r1
        del self.r2


if __name__ == "__main__":
    unittest.main()
