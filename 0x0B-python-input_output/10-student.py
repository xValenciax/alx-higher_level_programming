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
        that co-exist in the attrs param"""
        if attrs is not None:
            new_dict = {attr: self.__dict__[attr]
                        for attr in attrs if attr in list(self.__dict__.keys())}
            return new_dict

        return self.__dict__
