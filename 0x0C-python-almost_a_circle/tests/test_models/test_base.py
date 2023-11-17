#!/usr/bin/python3
"""
A module to test the base class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    Various tests to test Base Class
    """

    def setUp(self):
        """
        sets up the object
        """
        self.b1 = Base()
        self.b2 = Base(10)

    def test_init(self):
        """
        tests the init method
        """
        self.assertEqual(self.b1.id, None)
        self.assertEqual(self.b2.id, 10)

    def test_class_attribute(self):
        """
        tests the class attribute
        """
        self.assertEqual(Base._Base__nb_objects, 0)

    def tearDown(self):
        """
        teardown of objects
        """
        del self.b1
        del self.b2


if __name__ == "__main__":
    unittest.main()
