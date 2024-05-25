#!/usr/bin/python3


class SwimMixin:
    """
    A mixin class to provide swimming capability.
    """

    def swim(self):
        """
        Prints a message indicating that the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class to provide flying capability.
    """

    def fly(self):
        """
        Prints a message indicating that the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a Dragon that can both swim and fly.
    Inherits from SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Prints a message indicating that the dragon roars.
        """
        print("The dragon roars!")
