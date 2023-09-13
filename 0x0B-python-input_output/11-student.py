#!/usr/bin/python3
"""Student module"""


class Student:
    """represents a Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """converts a class into dictionary representation of attributes
        that co-exist in the attrs parameter"""
        if (isinstance(attrs, list)
                and all([isinstance(x, str) for x in attrs])):
            new_dict = {}
            for item in attrs:
                if item in list(self.__dict__.keys()):
                    new_dict[item] = self.__dict__[item]
            return new_dict

        return self.__dict__

    def reload_from_json(self, json):
        """replaces all instance attribute of class Student"""
        keys = list(json.keys())
        for key in keys:
            self.__dict__[key] = json[key]
