#!/usr/bin/python3
for c in range(100):
    if c < 10:
        print("0{}".format(c), end=', ')
    else:
        print("{}".format(c), end=', ')
