#!/usr/bin/python3

"""module that defines load from json file function"""
import json


def load_from_json_file(filename):
    """writes an object into a text file using JSON"""
    with open(filename, 'r', encoding='UTF-8') as f:
        return json.load(f)
