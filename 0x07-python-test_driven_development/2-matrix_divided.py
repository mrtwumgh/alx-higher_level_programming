#!/usr/bin/python3
"""
A module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of list)" +
                        "of integers/floats")

    if not all(isinstance(elem, (int, float))
       for row in matrix
       for elem in row):
        raise TypeError("matrix must be a matrix (list of list)" +
                        "of integers/floats")

    num_of_cols = len(matrix[0])
    for row in matrix:
        if num_of_cols != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
