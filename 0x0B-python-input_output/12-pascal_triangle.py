#!/usr/bin/python3
"""
A module that returns a list of lists of integers
representing the pascal's triangle
"""


def pascal_triangle(n):
    """
    a function that returns a pascal triangle
    """
    if n <= 0:
        return []
    else:
        result = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
        return result
