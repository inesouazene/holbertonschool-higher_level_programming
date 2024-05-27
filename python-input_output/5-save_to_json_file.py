#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Parameters:
    my_obj (any): The object to be serialized and written to the file.
    filename (str): The name of the file to write to.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
