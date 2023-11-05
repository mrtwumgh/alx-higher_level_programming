#!/usr/bin/python3
"""
A module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    a function that divieds all elements of a matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elem, int) or isinstance(elem, float))
                    for elem in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (lists of lists) of "
                        "integer/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
