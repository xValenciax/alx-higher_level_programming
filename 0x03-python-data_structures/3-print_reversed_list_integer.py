#!/usr/bin/python3
# AUTHOR Selim

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in reversed(range(len(my_list))):
            print("{:d}".format(my_list[i]))
