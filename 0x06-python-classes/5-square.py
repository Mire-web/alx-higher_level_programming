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
        self._Square__size = size

    def area(self):
        """ 
        Calculates the area of a Square.
        
        Returns:
              int: the area of a square.
        """
        return self._Square__size ** 2

    @property
    def size(self):
        """
        Gets the size of the square  object
        Returns:
            _Square__size: size of the square
        """
        return self._Square__size
    @size.setter
    def size(self, value):
        """
        Sets the value of the square size
        """
        if type(value) == int and value >= 0:
            self._Square__size = value
        elif type(value) == int and value < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """
        Prints out the square
        """
        if self._Square__size == 0:
            print("")
        else:
            row = self._Square__size
            column = self._Square__size
            while row > 0:
                while column > 0:
                    print("#", end="")
                    column -= 1
                print("")
                column = self._Square__size
                row -= 1
