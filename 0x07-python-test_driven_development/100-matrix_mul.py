#!/usr/bin/python3
"""
Module: Matrix Multiplication
Desc: Performs a multiplication of matrix
Author: Mire
"""

def matrix_mul(m_a, m_b):
    """Matrix Multiplication Function"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]
    for row_id in range(len(m_a)):
        for col_id in range(len(m_b[0])):
            col_no = 0
            for row in m_a[row_id]:
                result[row_id][col_id] += row * m_b[col_no][col_id]
                col_no += 1
    return result
