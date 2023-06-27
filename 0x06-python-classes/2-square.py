#!/usr/bin/python3
# 2-square.py
# Mire E Amah <amahe8664@gmail.com>
"""Create a Square"""

class Square:
    """Define the square"""
    def __init__(self, size=0):
        """Instantiate the square class
        Args: size=0: size of the square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
