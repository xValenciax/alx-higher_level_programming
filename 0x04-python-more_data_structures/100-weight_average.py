#!/usr/bin/python3
# AUTHORS Selim

def weight_average(my_list=[]):
    bast = 0
    maqam = 0
    for tup in my_list:
        bast += tup[0] * tup[1]
        maqam += tup[1]

    return bast / maqam if my_list else 0
