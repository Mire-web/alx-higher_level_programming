#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    i = 0
    for row in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, row)))
        i += 1
    return new_matrix
