#!/usr/bin/python3
# AUTHORS Selim

def complex_delete(a_dictionary, value):
    dict = a_dictionary.copy()
    for key, val in dict.items():
        if value == val:
            del a_dictionary[key]
    return a_dictionary
