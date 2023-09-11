#!/usr/bin/python3
"""module that defines inherits_from function"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class"""
    if obj.__class__ == a_class:
        return False
    return issubclass(type(obj), a_class)
