#!/usr/bin/python3\

"""This a Module that contains one class called Square"""


class Square:
    """Represents a Square, but it's empty for now"""

    def __init__(self, size=0):
        """initializes the data"""
        self.set_size(size)

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if not str(type(size)).__contains__('int'):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
