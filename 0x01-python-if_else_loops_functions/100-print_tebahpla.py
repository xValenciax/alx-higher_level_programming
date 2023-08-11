#!/usr/bin/python3

for i in reversed(range(97, 123)):
    c = i
    if i % 2 != 0:
        c = i - 32
    print("{}".format(chr(c)), end='')
