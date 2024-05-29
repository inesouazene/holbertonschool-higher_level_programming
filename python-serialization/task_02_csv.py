#!/usr/bin/python3
""" Task 02: CSV file processing """
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert data from a CSV file to JSON format and save it to data.json.

    Args:
    csv_filename (str): The name of the CSV file to read data from.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
