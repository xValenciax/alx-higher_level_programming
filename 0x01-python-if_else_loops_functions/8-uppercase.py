#!/usr/bin/python3
# Author - Selim

islower = __import__('7-islower').islower
def uppercase(str):
    """Function prints a string in uppercase."""
    for c in str:
        ch = c
        if islower(c):
            cc = ord(c) - 32
            ch = chr(cc)

        print(ch, end='')
    print()
