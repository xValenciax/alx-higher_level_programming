#!/usr/bin/python3
# AUTHORS Selim

def multiply_by_2(a_dictionary):
    dict = {}

    for key, value in a_dictionary.items():
        dict[key] = value*2
    return dict
