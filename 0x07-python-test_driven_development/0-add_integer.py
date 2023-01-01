#!/usr/bin/python3
"""
This contains a module that adds two integers
It has one function with two integer arguements
and returns an integer
"""


def add_integer(a, b=98):
    """ This functions adds two integers
    Args:
        a: integer
        b: integer
    Returns:
        integer
    """
    if (type(a) != int) and (type(a) != float):
        raise TypeError('a must be an integer')
    if (type(b) != int) and (type(b) != float):
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
