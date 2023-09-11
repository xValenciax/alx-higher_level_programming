#!/usr/bin/python3
"""module that defines is_same_class function"""


def is_same_class(obj, a_class):
    """checks if obj is instance of a_class"""
    return type(obj).__name__ == a_class.__name__
