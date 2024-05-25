#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the elements by.

    Returns:
        list of lists: A new matrix with elements divided by `div`,
        rounded to 2 decimal places.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers or floats,
                   or if `div` is not a number,
                   or if `div` is equal to 0.
        ValueError: If rows of `matrix` are not of the same size.
    """
    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(errorMessage)
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(errorMessage)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
