#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            print(f.read(), end="")
