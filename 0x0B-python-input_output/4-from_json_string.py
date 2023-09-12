#!/usr/bin/python3

"""module that defines from json string function"""
import json


def from_json_string(my_str):
    """converts a JSON string into an object representation"""
    return json.loads(my_str)
