#!/usr/bin/python3
class Square:
    """
    A class to define a Square with all it's properties
    Attributes:
        _Square__size: Size of the square.
    """
    def __init__(self, size=0):
        if type(size) == int and size >= 0:
            self._Square__size = int(size)
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
