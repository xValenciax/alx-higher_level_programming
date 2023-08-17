#!/usr/bin/python3
# AUTHOR Selim

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if col == len(matrix[row]) - 1:
                    print("{:d}".format(matrix[row][col]), end='')
                else:
                    print("{:d}".format(matrix[row][col]), end=' ')
            print()
