#!/usr/bin/python3
"""
An Object Lookup function
Author: Mire
"""


def lookup(obj):
    """
    Lookup Function
    arguments: Takes a Object as argument
    return: returns a list of methods and attributes of an object
    """

    return dir(obj)
