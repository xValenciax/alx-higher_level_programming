#!/usr/bin/python3
# AUTHOR Selim

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    return tuple_a[0] + tuple_b[0], tuple_b[1] + tuple_a[1]
