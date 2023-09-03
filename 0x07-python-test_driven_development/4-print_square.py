#!/usr/bin/python3

"""This Module defines a function that prints a square"""


def print_square(size):
    """
    prints a square with char #
    while handling any respective errors
    """
    if not isinstance(size, int) or (size < 0 and isinstance(size, float)):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
