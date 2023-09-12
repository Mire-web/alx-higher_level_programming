#!/usr/bin/python3
"""
A Square Class
Author: Mire
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square Class as from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
