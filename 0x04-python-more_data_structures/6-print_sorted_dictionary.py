#!/usr/bin/python3
# AUTHORS Selim

def print_sorted_dictionary(a_dictionary):
    """sorts a dictionary by its keys then print it"""
    for key, val in sorted(a_dictionary.items()):
        print("{}: {}".format(key, val))
