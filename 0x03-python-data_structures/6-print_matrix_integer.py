#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 1
    for row in matrix:
        for num in row:
            if i % 3 != 0:
                print('{:d}'.format(num), end=" ")
            else:
                print('{:d}'.format(num), end="")
            i += 1
        print()
