#!/usr/bin/python3
"""Defines a JSON file-reading function."""

import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object representation of the JSON data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
