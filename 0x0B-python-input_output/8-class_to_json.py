#!/usr/bin/python3
"""module that defines function class_to_json"""


def class_to_json(obj):
    """returns a dictionary description
    for JSON serialization of an obj"""
    return obj.__dict__
