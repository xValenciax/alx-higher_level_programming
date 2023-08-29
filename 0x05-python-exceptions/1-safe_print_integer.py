#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if not str(type(value)).__contains__('int'):
            raise TypeError
        print('{:d}'.format(value))
    except TypeError:
        return False
    else:
        return True
