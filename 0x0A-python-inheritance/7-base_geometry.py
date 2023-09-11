#!/usr/bin/python3
"""module that defines BaseGeometry Class"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
