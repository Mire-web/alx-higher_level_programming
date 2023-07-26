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
    def __init__(self, size=0, position=(0, 0)):
        self._Square__size = size
        self._position = position

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
        Attributes:
              value: value for size of the square
        """
        if type(value) == int and value >= 0:
            self._Square__size = value
        elif type(value) == int and value < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """
        Gets the position value of the square
        
        Returns: the position of the square as a tuple
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Sets the value for the position of the Square
        
        Attributes:
            value: a tuple containing the position coordinates
        """
        only_positive_num = all(num > 0 for num in value)
        if type(value) == tuple and only_positive_num:
            self._position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        Prints out the square
        """
        if self._Square__size == 0:
            print("")
        else:
            row = self._Square__size
            column = self._Square__size
            position = self._position
            if position[1] > 0:
                for i in range(position[1]):
                    print("")
            while row > 0:
                for i in range(position[0]):
                    print(" ", end="")
                while column > 0:
                    print("#", end="")
                    column -= 1
                print("")
                column = self._Square__size
                row -= 1
