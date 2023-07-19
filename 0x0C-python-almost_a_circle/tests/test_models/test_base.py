#!/usr/bin/python3
"""
Tests for the class base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBaseClass(unittest.TestCase):
    """
    test methods
    """
    def test_id(self):
        """
        test attribute id
        """
        Base._Base__nb_objects = 0
        base_1 = Base()
        base_2 = Base()
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 2)

    def test_set_id(self):
        """
        tests setting id
        """
        base_5 = Base(12)
        self.assertEqual(base_5.id, 12)

    def test_nb_objects(self):
        """
        test class attribute nb_objects
        """
        Base._Base__nb_objects = 0
        base_3 = Base()
        base_4 = Base()
        self.assertEqual(base_3.id, 1)
        self.assertEqual(base_4.id, 2)

    def test_to_json_string(self):
        """
        test to_json method
        """

        list_dictionaries = [
                {'id': 1,
                 'width': 10,
                 'height': 7,
                 'x': 2,
                 'y': 8
                 },
                {'id': 2,
                 'width': 2,
                 'height': 4,
                 'x': 0,
                 'y': 0
                 }
        ]
        s1 = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},'
        s2 = ' {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        output = s1 + s2
        self.assertEqual(Base.to_json_string(list_dictionaries), output)

        list_dictionaries = []
        self.assertEqual(Base.to_json_string(list_dictionaries), "[]")

        list_dictionaries = None
        self.assertEqual(Base.to_json_string(list_dictionaries), "[]")

    def test_save_to_file(self):
        """
        tests the save_to_file method
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        s1 = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},'
        s2 = ' {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        output = s1 + s2
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), output)

    def test_from_json_string(self):
        """
        tests the from_json_string method
        """
        list_input = [{'id': 89, 'width': 10}]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'id': 89, 'width': 10}])

    def test_create(self):
        """
        tests the create method
        """
        Base._Base__nb_objects = 0
        b1 = Rectangle.create(id=42, width=3, height=4)
        self.assertEqual(b1.id, 42)
        self.assertEqual(b1.width, 3)
        self.assertEqual(b1.height, 4)

        b2 = Square.create(id=24, size=5)
        self.assertEqual(b2.id, 24)
        self.assertEqual(b2.size, 5)

    def test_load_from_file(self):
        """
        tests the load_from_file method
        """
        Base._Base__nb_objects = 0
        Base.save_to_file([])
        self.assertEqual(Base.load_from_file(), [])

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output), 2)

        self.assertEqual(list_rectangles_output[0].__dict__, r1.__dict__)
        self.assertEqual(list_rectangles_output[1].__dict__, r2.__dict__)

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        self.assertEqual(Square.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
