#!/usr/bin/python3
""" Task 01: Custom Object Serialization"""
import pickle


class CustomObject:
    """ A class to represent a custom object. """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of CustomObject and
        save it to the provided filename.

        Args:
        filename (str): The name of the file where the object
        should be serialized.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred while saving the object '{e}'")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from the provided filename.

        Args:
        filename (str): The name of the file to deserialize the object from.

        Returns:
        CustomObject: An instance of CustomObject if successful,
        None otherwise.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"An error occurred while loading the object from '{e}'")
            return None
