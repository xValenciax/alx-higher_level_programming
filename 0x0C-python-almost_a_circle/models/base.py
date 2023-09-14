#!/usr/bin/python3
"""this is a module that defines the Base Class"""


class Base:
    """represents a Base class for all future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes an instance of the class"""
        type(self).__nb_objects += 1
        self.id = type(self).__nb_objects
        if id is not None:
            self.id = id
