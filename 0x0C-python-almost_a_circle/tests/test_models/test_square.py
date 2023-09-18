#!/usr/bin/python3

"""module that creates unit tests for Base class"""

import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Rectangle._Base__nb_objects = 0
        cls.output_buffer = StringIO()
        sys.stdout = cls.output_buffer

    @classmethod
    def tearDownClass(cls):
        sys.stdout = sys.__stdout__
        cls.output_buffer.close()

    def setUp(self):
        Base._Base__nb_objects = 0
        self.output_buffer.truncate(0)
        self.output_buffer.seek(0)

    def test_type(self):
        square = Square(4, 2, 2)
        self.assertTrue(isinstance(square, Base))
        self.assertTrue(isinstance(square, Rectangle))
        self.assertTrue(isinstance(square, Square))
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Base))
        self.assertFalse(isinstance(Square, Rectangle))

    def test_attrs(self):
        square = Square(4, 2, 2)
        self.assertEqual(square.id, 1)
        square.id = 10
        self.assertEqual(square.id, 10)

        with self.assertRaises((ValueError, TypeError)):
            square.width = -10
            square.x = -10
            square.y = 'hello'

        print(square)
        output = self.output_buffer.getvalue()
        self.assertEqual(output, '[Square] (10) 2/2 - 4\n')

        with self.assertRaises((ValueError, TypeError)):
            square.size = -10
            square.size = 'size'

    def test_update(self):
        square = Square(4, 2, 2)
        square.update(5, 10, 2, 2)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)

        square.update(size=12, x=1, y=1, id=10)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 12)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 1)

        with self.assertRaises((TypeError, ValueError)):
            square.update('hello')
            square.update(x=-1)
            square.update(y=1, size='size')


if __name__ == '__main__':
    unittest.main()
