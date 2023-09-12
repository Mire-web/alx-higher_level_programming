#!/usr/bin/python3
"""
Class Attribute Adder
Author: Mire
"""


def add_attribute(obj, key, value):
    """Adds Attribute to a class"""
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__') and
                                    key in type(obj).__slots__):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
