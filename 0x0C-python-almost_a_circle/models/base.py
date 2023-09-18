#!/usr/bin/python3
"""this is a module that defines the Base Class"""

import json


class Base:
    """represents a Base class for all future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes an instance of the class"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
