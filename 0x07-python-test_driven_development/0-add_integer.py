#!/usr/bin/python3

"""A Module that defines an Add function"""


def add_integer(a, b=98):
    """
    returns the addition result of a and b
    while also handling any respective errors
    this method is tested using doctest module
    """

    ai = a
    bi = b
    if isinstance(a, float):
        ai = int(a)
    if isinstance(b, float):
        bi = int(b)

    if not isinstance(ai, int):
        raise TypeError('a must be an integer')
    elif not isinstance(bi, int):
        raise TypeError('b must be an integer')
    else:
        return ai + bi
