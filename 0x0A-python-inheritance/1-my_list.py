#!/usr/bin/python3
"""
List class that inherits from main list
Author: Mire
"""


class MyList(list):
    """A Subclass of the python list class"""

    def print_sorted(self):
        """Sorts the list in ascending order"""
        new_list = self[:]
        new_list.sort()
        print(new_list)
