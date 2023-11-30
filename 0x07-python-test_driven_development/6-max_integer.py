#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(mlist=[]):
        """Function to find and return the max integer in a list of integers
           If the list is empty, the function returns None
        """
        if len(mlist) == 0:
            return None
        result = mlist[0]
        i = 1
        while i < len(mlist):
                if mlist[i] > result:
                        result = mlist[i]
                i += 1
        return result
