#!/usr/bin/python3
"""this is a module that defines the Base Class"""

import json
import os


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
        """
        a static method that converts a list of dictionaries
        to json format
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        a class method that saves a list of objects of type cls
        into a json file
        """
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
        """
        a static method that takes a json string
        and converts it into appropriate obj
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        a class method that creates an obj of type cls
        based attributes passed in a dictionary
        """
        obj = cls(1, 1, 1, 1) if cls.__name__ == 'Rectangle' else cls(1, 1, 1)

        obj.update(**dictionary)

        return obj

    @classmethod
    def load_from_file(cls):
        """
        a class method that loads a data from a json file
        """
        filename = '{}.json'.format(cls.__name__)
        file_content = ""

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            file_content = f.read()

        list_content = cls.from_json_string(file_content)

        data_to_return = []

        for dic in list_content:
            data_to_return.append(cls.create(**dic))

        return data_to_return
