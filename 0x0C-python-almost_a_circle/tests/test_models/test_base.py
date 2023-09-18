#!/usr/bin/python3

"""module that creates unit tests for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """unit tests class for Base class"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_id(self):
        base_with_empty_id = Base()
        self.assertEqual(base_with_empty_id.id, 1)

    def test_id_as_param(self):
        base_with_given_id = Base(11)
        self.assertEqual(base_with_given_id.id, 11)

    def test_id_increments(self):
        base_id_increments = Base()
        self.assertEqual(base_id_increments.id, 2)

    def test_no_objects_inaccessible(self):
        base = Base()
        with self.assertRaises(AttributeError):
            print(base.__nb_objects)
