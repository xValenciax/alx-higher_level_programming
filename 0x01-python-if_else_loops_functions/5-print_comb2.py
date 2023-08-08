#!/usr/bin/python3
for c in range(100):
    if c % 99 or c == 0:
        print("{:0>2}".format(c), end=', ')
    else:
        print("{}".format(c))
