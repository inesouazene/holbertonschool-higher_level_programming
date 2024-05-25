#!/usr/bin/python3
"""contains the MyList class"""


class MyList(list):
    """subclass of list"""
    def print_sorted(self):
        """print sorted list"""
        sort_list = super().copy()
        sort_list.sort()
        print(sort_list)
