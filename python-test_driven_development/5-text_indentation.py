#!/usr/bin/python3
"""
This module provides a function called ``text_indentation()``
which prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints the text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ".?:":
        text = text.replace(delimiter, delimiter + "\n\n")

    lines = [line.strip() for line in text.split("\n")]

    formatted_text = "\n".join(lines)
    print(formatted_text, end="")
