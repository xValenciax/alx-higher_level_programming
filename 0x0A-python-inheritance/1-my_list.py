#!/usr/bin/python3
"""module that defines a MyList class"""


class MyList(list):
    """MyList class that inherits from list superclass"""

    def print_sorted(self):
        """prints a list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
