#!/usr/bin/python3
# AUTHOR Selim

def no_c(my_string):
    if my_string:
        new_str = [c for c in my_string if c not in 'cC']
        return str.join("", new_str)
