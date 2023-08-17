#!/usr/bin/python3
# AUTHORS Selim

def roman_to_int(roman_string):
    if roman_string == None or str(type(roman_string)) != "<class 'str'>":
        return 0

    rc = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    deuce = False
    number = 0

    for i, key in enumerate(roman_string):
        if i + 1 < len(roman_string) and rc[key] < rc[roman_string[i + 1]]:
            number += (rc[roman_string[i + 1]] - rc[key])
            deuce = True
        elif deuce:
            deuce = False
        else:
            number += rc[roman_string[i]]

    return number
