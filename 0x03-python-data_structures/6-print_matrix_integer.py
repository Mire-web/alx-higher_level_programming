#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        for num in row:
            if i != len(matrix)-1:
                print('{:d}'.format(num), end=" ")
            else:
                print('{:d}'.format(num), end="")
        print()
        i++
