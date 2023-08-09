#!/usr/bin/python3
# Author - Selim

def fizzbuzz():
    """function that prints number up to 100 separated by spaces"""
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print("{}".format(i), end=' ')
