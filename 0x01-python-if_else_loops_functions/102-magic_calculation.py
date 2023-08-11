#!/usr/bin/env python3

def magic_calculation(a, b, c):
    """performs some magic calculations on params"""
    if b < a:
        if b > c:
            return (a * b) - c
        else:
            return a + b
    return c
