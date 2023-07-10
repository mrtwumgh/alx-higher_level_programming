#!/usr/bin/python3
"""
A module that divides elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides elements of a matrix
    returns the new matrix

    Args:
        matrix: the matrix
        div: the divisor
    """
    new_matrix = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    rows = len(matrix[0])
    for row in matrix:
        if len(row) != rows:
            raise TypeError("Each row of the matrix must be the same size")
        elem_list = []
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(msg)
            elem_result = round(elem / div, 2)
            elem_list.append(elem_result)
        new_matrix.append(elem_list)
    return new_matrix
