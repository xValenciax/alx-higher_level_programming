#!/usr/bin/python3

"""
This Module is a unit test module
that tests the max_integer module
using unittest module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """a test case class for max_integer function in max integer module"""

    def test_max_integer(self):
        """unit test function for max_integer function"""
        # valid input => correct output
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([2, 5, 3, 6, 1, 8]), 8)
        self.assertEqual(max_integer([1, 1, 1, 1, 1,]), 1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer('string'), 't')
        self.assertEqual(max_integer(['hello', 'world', 'wtf']), 'wtf')
        self.assertEqual(max_integer(['a', 'c', 'd', 'f', 'b']), 'f')
        self.assertEqual(max_integer((1, 8, 5, 2, 10, 3)), 10)
        self.assertEqual(max_integer([True, False, 3, 2]), 3)

        # raises TypeError exception
        with self.assertRaises(TypeError):
            max_integer(1)
            max_integer(['hello', True, 'a', 15])

        # raises KeyError exception
        with self.assertRaises(KeyError):
            max_integer({'name': "Mohamed", 'age': 30})
