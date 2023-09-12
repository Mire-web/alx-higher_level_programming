#!/usr/bin/python3
"""
Same Object Checker
Author: Mire
"""


def inherits_from(obj, a_class):
    """Checks if object is a subclass of a class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
