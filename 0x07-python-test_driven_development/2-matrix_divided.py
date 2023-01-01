#!/usr/bin/python3
""" Functions that divides matrix elements"""


def matrix_divided(matrix, div):
    """
    The function that divides matrix elements
    Args:
        matrix: nested list of int or float
        div: an int or float divisor
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    if all(list(map(lambda x: x == list, list(map(type, matrix))))) is False:
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    if all(list(map(lambda x: all(list(map(lambda x: type(x) == int or
                                  type(x) == float, x))), matrix))) is False:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if all(list(map(lambda x: len(x) == len(matrix[0]), matrix))) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError("division by zero")
    m = list(map(lambda x: list(map(lambda x: round(x / div, 2), x)), matrix))
    return m
