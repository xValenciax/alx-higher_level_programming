#!/usr/bin/python3\

"""This a Module that contains one class called Square"""


class Square:
    """Represents a Square, but it's empty for now"""

    def __init__(self, size=0):
        """initializes the data"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not str(type(size)).__contains__('int'):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        return self.size ** 2
