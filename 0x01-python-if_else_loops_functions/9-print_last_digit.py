#!/usr/bin/python3
# Author - Selim

def print_last_digit(number):
    """Function that prints the last digit of a number"""
    if number < 0:
        number = number * -1
    last_dig = number % 10
    print(last_dig, end='')
    return last_dig
