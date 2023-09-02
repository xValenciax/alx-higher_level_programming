#!/usr/bin/python3

"""A Module that defines an Add function"""


def say_my_name(first_name, last_name=""):
    """
    prints the string my name is <first name> <last name>
    while also handling any respective errors
    """
    if not isinstance(first_name, str):
        raise TypeError(
            'first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    if last_name:
        print('My name is {} {}'.format(first_name, last_name))
    else:
        print('My name is {}'.format(first_name))
