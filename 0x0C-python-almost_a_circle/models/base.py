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

    @classmethod
    def save_to_file(cls, list_objs):
        content_to_be_saved = []
        filename = "{}.json".format(cls.__name__)

        if list_objs is not None:
            for obj in list_objs:
                content_to_be_saved.append(obj.to_dictionary())

        json_data = Base.to_json_string(content_to_be_saved)

        with open(filename, 'w') as f:
            f.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)
