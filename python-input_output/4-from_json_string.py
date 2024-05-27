#!/usr/bin/python3
"""Module for from_json_string method"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Parameters:
    my_str (str): The JSON string to be deserialized.

    Returns:
    any: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
