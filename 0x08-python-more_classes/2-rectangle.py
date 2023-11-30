#!/usr/bin/python3
"""
Rectancle Module
=================
Author: Mire
"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value=0):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        Calcualates the area of a rectangle
        returns: the area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of a rectangle
        return: the pewrimeter of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
