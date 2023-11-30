#!/usr/bin/python3
"""
Base Geometry Class
Author: Mire
"""


class BaseGeometry:
    """
    The Base Geometry Class
    """

    def area(self):
        """Defines the area of a geometric shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Integer data"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
