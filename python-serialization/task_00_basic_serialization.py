#!/usr/bin/python3
""" Task 00: Basic Serialization"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
    data (dict): The Python dictionary to serialize.
    filename (str): The filename of the output JSON file.
    If the output file already exists it should be replaced.
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)
        print(f"Data serialized and saved to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while saving data to '{filename}': {e}")


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file to a Python dictionary.

    Args:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: The deserialized Python dictionary.
    """
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        print(f"An error occurred while loading data from '{filename}': {e}")
        return None
