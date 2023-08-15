#!/usr/bin/python3
# AUTHOR Selim

def no_c(my_string):
    if not my_string:
        return my_string

    new_str = [c for c in my_string if c not in 'cC']
    return str.join("", new_str)
