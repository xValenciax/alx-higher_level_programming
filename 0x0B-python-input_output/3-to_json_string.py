#!/usr/bin/python3

"""module that defines to json string function"""
import json


def to_json_string(my_obj):
    """converts an object into a JSON string representation"""
    return json.dumps(my_obj)
