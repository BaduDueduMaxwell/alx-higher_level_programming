#!/usr/bin/python3
"""This module defines Pascal's triangle"""


def pascal_triangle(n):
    """This function returns list of lists integers\
representating Pascal's triangle"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
