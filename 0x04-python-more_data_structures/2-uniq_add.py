#!/usr/bin/python3
# AUTHORS Selim

def uniq_add(my_list=[]):
    uniq_ints = set(my_list)
    sum = 0
    for int in uniq_ints:
        sum += int
    return sum
