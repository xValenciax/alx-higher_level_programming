#!/usr/bin/python3
"""Module to multiply two matrices"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices together"""

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all([isinstance(x, list) for x in m_a]):
        raise TypeError('m_a must be a list of lists')
    elif not all([isinstance(x, list) for x in m_b]):
        raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if not all([all([
            (isinstance(i, int) or isinstance(i, float)) for i in x]
    ) for x in m_a]):
        raise TypeError('m_a should contain only integers or floats')
    elif not all([all([
            (isinstance(i, int) or isinstance(i, float)) for i in x]
    ) for x in m_b]):
        raise TypeError('m_b should contain only integers or floats')

    if len(set([len(x) for x in m_a])) != 1:
        raise TypeError('each row of m_a must be of the same size')
    if len(set([len(x) for x in m_b])) != 1:
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []

    for row in range(len(m_a)):
        new_row = []
        for col in range(len(m_b[0])):
            new_element = 0
            for ele in range(len(m_a[row])):
                new_element += m_a[row][ele] * m_b[ele][col]
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix
