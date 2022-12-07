#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_a = []
    for row in matrix:
        list_a = []
        for column in row:
            list_a.append(column ** 2)
        matrix_a.append(list_a)
    return matrix_a
