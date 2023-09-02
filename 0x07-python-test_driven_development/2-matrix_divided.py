#!/usr/bin/python3

"""A Module that defines an Add function"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    while also handling any respective errors
    """
    div_i = int(div) if isinstance(div, float) else div

    if (not isinstance(matrix, list) or not all([isinstance(x, list) for x in matrix])
        or not all([all([isinstance(
            int(i) if isinstance(i, float) else i, int) for i in x]) for x in matrix])):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    elif len(set([len(x) for x in matrix])) != 1:
        raise TypeError('Each row of the matrix must have the same size')
    elif not isinstance(div_i, int):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(i / div, 2) for i in x] for x in matrix]
