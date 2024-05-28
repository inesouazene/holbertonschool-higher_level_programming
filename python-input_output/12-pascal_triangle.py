#!/usr/bin/python3
"""Generates Pascal's triangle up to n rows."""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
    n (int): The number of rows in Pascal's Triangle.

    Returns:
    list: A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the triangle

    for current_row in range(1, n):
        row = [1]  # Start each row with a 1
        for element_index in range(1, current_row):
            row.append(triangle[current_row - 1][element_index - 1]
                       + triangle[current_row - 1][element_index])
        row.append(1)  # End each row with a 1
        triangle.append(row)

    return triangle
