#!/usr/bin/python3
"""
Rectangle Class
Author: Mire
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defining the Rectangle Class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Defines the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of the rectangle class"""
        return f"[Rectangle] {self.__width}/{self.__height}"
