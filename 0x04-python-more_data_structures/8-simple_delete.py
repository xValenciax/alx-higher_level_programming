#!/usr/bin/python3
# AUTHORS Selim

def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key):
        del a_dictionary[key]
        return a_dictionary
    return a_dictionary
