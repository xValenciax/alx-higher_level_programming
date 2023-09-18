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

        self.basic_rect.display()
        output = self.output_buffer.getvalue()

        self.assertEqual(output, '\n\n  ##\n  ##\n')

    def test_class_str(self):
        print(self.basic_rect)
        output = self.output_buffer.getvalue()

        self.assertEqual(output, '[Rectangle] (3) 2/2 - 2/2\n')

    def test_wrong_params(self):
        with self.assertRaises(TypeError):
            r_t = Rectangle(1)
            r_t = Rectangle()
            r_t = Rectangle(2, 2)
            r_t.area('hello')
            r_t.display(1)

    def test_update(self):
        self.basic_rect.update(10, 3, 4, 5, 1)
        print(self.basic_rect)

        output = self.output_buffer.getvalue()

        self.assertEqual(output, '[Rectangle] (10) 5/1 - 3/4\n')

        with self.assertRaises((TypeError, ValueError)):
            self.basic_rect.update(10, 'hello', 4, 5, 1)
            self.basic_rect.update(10, 3, 0, 5, -1)
            self.basic_rect.update('hello')

        self.basic_rect.update(10)
        self.assertEqual(self.basic_rect.id, 10)

    def test_update_2(self):
        test_rect = Rectangle(10, 10, 10, 10)
        test_rect.update(height=1)
        self.assertEqual(test_rect.height, 1)

    def test_to_dictionary(self):
        rect = Rectangle(10, 2, 1, 9)
        r_dict = rect.to_dictionary()

        rect_2 = Rectangle(5, 1, 1, 9)
        r2_dict = rect_2.to_dictionary()
        self.assertFalse(r_dict == r2_dict)

        with self.assertRaises(TypeError):
            rect.to_dictionary(1)

    def test_to_json_string(self):
        r = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(9, 6, 1, 7)
        json_dictionary = Base.to_json_string(
            [r.to_dictionary(), r2.to_dictionary()])

        self.assertEqual(
            json_dictionary,
            '[{"id": 6, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 7, "width": 9, "height": 6, "x": 1, "y": 7}]')


if __name__ == '__main__':
    unittest.main()
