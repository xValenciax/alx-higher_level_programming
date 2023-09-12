#!/usr/bin/python3

"""module that defines the read file function"""


def read_file(filename=""):
    """reads a file and prints its content"""
    content = ""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    print(content)
