#!/usr/bin/python3
# Author - Selim

islower = __import__('7-islower').islower
def uppercase(str):
    """Function prints a string in uppercase."""
    for i in range(len(str)):
        ch = str[i]
        if islower(str[i]):
            ch = chr(ord(str[i]) - 32)
        if i != len(str) - 1:
            print("{}".format(ch), end='')
        else:
            print("{}".format(ch))
