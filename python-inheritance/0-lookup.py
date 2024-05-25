#!/usr/bin/python3
"""Defines an lookup object attribute function."""


def lookup(obj):
    """Return the list of available attributes and methods of an object"""
    return (dir(obj))
