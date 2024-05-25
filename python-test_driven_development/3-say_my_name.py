#!/usr/bin/python3
"""
This module provides a function called ``say_my_name()``
which prints a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name of the person.

    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
