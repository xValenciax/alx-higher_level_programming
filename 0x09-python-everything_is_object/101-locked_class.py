#!/usr/bin/python3
"""
defines LockedClass
"""


class LockedClass:
    """represents a class that only accepts first_name as an attribute"""

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'")
        super().__setattr__(name, value)
