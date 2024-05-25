#!/usr/bin/python3


class VerboseList(list):
    """
    A subclass of the built-in list that prints a notification message
    every time an item is added or removed.
    """

    def append(self, item):
        """
        Appends an item to the list and prints a notification message.

        Parameters:
        - item: The item to be added to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extends the list by appending elements from the iterable
        and prints a notification message.

        Parameters:
        - iterable: An iterable of items to be added to the list.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Removes the first occurrence of an item from the list
        and prints a notification message.

        Parameters:
        - item: The item to be removed from the list.

        Raises:
        - ValueError: If the item is not present in the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Removes and returns the item at the given position in the list
        and prints a notification message. If no index is specified,
        the last item is removed.

        Parameters:
        - index: The position of the item to remove (default is -1).

        Returns:
        - The item that was removed from the list.

        Raises:
        - IndexError: If the list is empty or the index is out of range.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
