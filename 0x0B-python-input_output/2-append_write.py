#!/usr/bin/python3

"""module that defines the append_write file function"""


def append_write(filename="", text=""):
    """appends a string to a text file and returns the number
    of characters added"""
    with open(filename, 'a', encoding='UTF-8') as f:
        return f.write(text)
