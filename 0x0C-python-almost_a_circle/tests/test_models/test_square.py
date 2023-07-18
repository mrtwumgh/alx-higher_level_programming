#!/usr/bin/python3
"""
A module to test the class Square
"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    methods to test the class
    """
    def test_init(self):
        """
        tests initialization
        """
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

        s1 = Square(3, 1, 2, 99)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 99)

    def test_str(self):
        """
        tests string representation
        """
        s = Square(5)
        output = f"[Square] ({s.id}) {s.x}/{s.y} - {s.width}"
        self.assertEqual(str(s), output)

    def test_size_getter(self):
        """
        tests getter
        """
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """
        tests setter
        """
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)


    def test_size_setter_invalid_value(self):
        """
        tests invalid value
        """
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "not an int"
        with self.assertRaises(ValueError):
            s.size = -1

    def test_args(self):
        """
        test args
        """
        s = Square(3)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_kwargs(self):
        """
        test kwargs
        """
        s = Square(3)
        s.update(id=1, size=2, x=3, y=4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        

if __name__ == "__main__":
    unittest.main()
