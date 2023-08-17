#!/usr/bin/python3
# AUTHOR Selim

def divisible_by_2(my_list=[]):
    ret_list = []

    for item in my_list:
        ret_list.append(True if item % 2 == 0 else False)
    return ret_list
