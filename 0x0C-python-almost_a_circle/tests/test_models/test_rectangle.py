#!/usr/bin/python3

"""module that creates unit tests for Base class"""

import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Unit test case for class Rectangle"""

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls.output_buffer = StringIO()
        sys.stdout = cls.output_buffer

        cls.rect_with_no_id = Rectangle(10, 5, 3, 4)
        cls.rect_with_id = Rectangle(5, 10, 4, 3, 12)
        cls.rect_with_no_x_y = Rectangle(2, 8)
        cls.basic_rect = Rectangle(2, 2, 2, 2)

    @classmethod
    def tearDownClass(cls):
        sys.stdout = sys.__stdout__
        cls.output_buffer.close()

        del cls.output_buffer
        del cls.rect_with_id
        del cls.rect_with_no_id
        del cls.rect_with_no_x_y
        del cls.basic_rect

    def setUp(self):
        self.output_buffer.truncate(0)
        self.output_buffer.seek(0)

    def test_types(self):
        self.assertTrue(isinstance(self.basic_rect, Rectangle))
        self.assertTrue(isinstance(self.basic_rect, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_no_id(self):
        self.assertEqual(self.rect_with_no_id.id, 1)
        self.assertEqual(self.rect_with_no_id.width, 10)
        self.assertEqual(self.rect_with_no_id.height, 5)
        self.assertEqual(self.rect_with_no_id.x, 3)
        self.assertEqual(self.rect_with_no_id.y, 4)

    def test_id_given(self):
        self.assertEqual(self.rect_with_id.id, 12)
        self.assertEqual(self.rect_with_id.width, 5)
        self.assertEqual(self.rect_with_id.height, 10)
        self.assertEqual(self.rect_with_id.x, 4)
        self.assertEqual(self.rect_with_id.y, 3)

    def test_no_x_y(self):
        self.assertEqual(self.rect_with_no_x_y.id, 2)
        self.assertEqual(self.rect_with_no_x_y.width, 2)
        self.assertEqual(self.rect_with_no_x_y.height, 8)
        self.assertEqual(self.rect_with_no_x_y.x, 0)
        self.assertEqual(self.rect_with_no_x_y.y, 0)

    def test_non_valid_attrs(self):
        with self.assertRaises((ValueError, TypeError)):
            self.basic_rect.width = -10
            self.basic_rect.height = 0
            self.x = '10'
            self.y = -1

    def test_area(self):
        self.assertEqual(self.basic_rect.area(), 4)
        self.assertEqual(self.rect_with_id.area(), 50)

    def test_display(self):
        self.rect_with_no_x_y.display()
        output = self.output_buffer.getvalue()

        self.assertEqual(output, '##\n##\n##\n##\n##\n##\n##\n##\n')

        self.output_buffer.truncate(0)
        self.output_buffer.seek(0)

