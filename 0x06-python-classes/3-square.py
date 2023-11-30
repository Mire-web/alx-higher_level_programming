#!/usr/bin/python3
"""
Author: Mire
Description: A Sqaure class project for Alx
"""
class Square:
    """
    A class defining a square with all it's properties
    Attribute:
       _Square__size: Size of the sqaure
    """
    def __init__(self, size=0):
        if type(size) == int and size >= 0:
            self._Square__size = size
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self._Square__size ** 2
