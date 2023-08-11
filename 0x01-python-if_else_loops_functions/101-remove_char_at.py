#!/usr/bin/python3

def remove_char_at(str, n):
    """removes a specific char at index n"""
    return str[:n] + str[n+1:]
