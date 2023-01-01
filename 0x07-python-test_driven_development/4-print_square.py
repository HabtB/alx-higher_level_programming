#!/usr/bin/python3
""" This module prints a square using hash """


def print_square(size):
    """
    This function prints a square with
    size, size.
    Args:
        size: the size of the square
    """
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        for i in range(size):
            print('#' * size)
    else:
        raise TypeError("size must be an integer")
