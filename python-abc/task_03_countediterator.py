#!/usr/bin/python3


class CountedIterator:
    """
    A class that extends the built-in iterator
    to count the number of items iterated over.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable.

        Parameters:
        - iterable: An iterable from which the iterator is created.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        Returns the next item from the iterator and increments the counter.

        Returns:
        - The next item from the iterator.

        Raises:
        - StopIteration: When there are no more items to iterate.
        """
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        """
        Returns the current count of iterated items.

        Returns:
        - int: The number of items iterated over.
        """
        return self.counter
