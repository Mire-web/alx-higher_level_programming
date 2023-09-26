#!/usr/bin/python3
"""
Module: Test Max integer
Desc: unit test for the function max_integer
Tester: Mire
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for Max_integer function"""

    def test_int_list(self):
        """Test normal input"""
        self.assertEqual(max_integer([1,2,3,4,34,4]), 34)
        self.assertEqual(max_integer([23, -1, 23, 20]), 23)

    def test_negative_int(self):
        """Test negative numbers"""
        self.assertEqual(max_integer([0,-1,-20,-4]), 0)
        self.assertEqual(max_integer([-2,-3,-5,-1]), -1)

    def test_empty_list(self):
        """Test empty list input"""
        self.assertEqual(max_integer([]), None)
