#!/usr/bin/python3

"""
defines LockedClass
"""


class LockedClass:
    """represents a class that only accepts first_name as an attribute"""

    def __setattr__(self, __name, __value):
        if __name != 'first_name':
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{__name}'")
        super().__setattr__(__name, __value)
