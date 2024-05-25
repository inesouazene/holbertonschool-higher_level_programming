#!/usr/bin/python3


class Fish:
    """
    Represents a Fish with methods to swim and describe its habitat.
    """

    def swim(self):
        """
        Prints a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints a message indicating that the fish lives in water.
        """
        print("The fish lives in water")


class Bird:
    """
    Represents a Bird with methods to fly and describe its habitat.
    """

    def fly(self):
        """
        Prints a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints a message indicating that the bird lives in the sky.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a FlyingFish that can both swim and fly,
    inheriting from Fish and Bird.
    """

    def swim(self):
        """
        Prints a message indicating that the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Prints a message indicating that the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Prints a message indicating that the flying fish
        lives both in water and the sky.
        """
        print("The flying fish lives both in water and the sky!")
