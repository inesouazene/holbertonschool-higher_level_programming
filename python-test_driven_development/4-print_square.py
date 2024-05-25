#!/usr/bin/python3
"""
This module defines a function called print_square.
The print_square function prints a square with the character '#'.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Returns:
        None
    """
    errorMessage = "size must be an integer"
    if not isinstance(size, int):
        raise TypeError(errorMessage)
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError(errorMessage)
    for index in range(size):
        print("#" * size)
