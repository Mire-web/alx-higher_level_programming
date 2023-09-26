#!/usr/bin/python3
"""
Module: Matrix divisor
Desc: A function that divides all elements of a matrix by given divisor
Author: Mire
"""

def matrix_divided(matrix, div):
    new_matrix = []
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        for i in range(len(matrix)):
            if type(matrix[i]) is not list:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(matrix[i]) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
        for row in matrix:
            for col in row:
                if type(col) != int and type(div) != float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if type(div) != int and type(div) != float:
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")
        else:
            for row in matrix:
                matrix_copy = []
                for col in row:
                    matrix_copy.append(round(col/div, 2))
                new_matrix.append(matrix_copy)
    return new_matrix
