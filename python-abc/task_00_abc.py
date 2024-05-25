#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal class"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """
    class Dog that inherit from Animal class
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    class Cat that inherit from Animal class
    """
    def sound(self):
        return "Meow"
