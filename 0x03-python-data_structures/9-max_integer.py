#!/usr/bin/python3
# AUTHOR Selim

def max_integer(my_list=[]):
    if not my_list:
        return None

    max = my_list[0]
    for i in my_list:
        max = i if i >= max else max

    return max
