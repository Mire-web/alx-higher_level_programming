#!/usr/bin/python3
"""
My integer class
Author: Mire
"""


class MyInt(int):
    """My Int Class"""

    def __eq__(self, other):
        """My equality method"""
        return self.real != other

    def __ne__(self,  other):
        """My inequality method"""
        return self.real == other
