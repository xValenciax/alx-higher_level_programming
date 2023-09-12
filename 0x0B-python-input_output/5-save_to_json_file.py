#!/usr/bin/python3

"""module that defines save to json string function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object into a text file using JSON"""
    with open(filename, 'w', encoding='UTF-8') as f:
        return json.dump(my_obj, f)
