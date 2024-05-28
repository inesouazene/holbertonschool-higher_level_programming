#!/usr/bin/python3
"""Class Student that defines a student"""


class Student:
    """
    Defines a student by:
    - first_name
    - last_name
    - age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained
        in this list are retrieved.
        Otherwise, all attributes are retrieved.

        Args:
            attrs: List of attribute names to include in the dictionary.

        Returns:
            dict: A dictionary containing the specified attributes
            of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key in json:
            self.__dict__[key] = json[key]
