#!/usr/bin/python3
""" Class Square: defines a class with an instant variable size """


class Square:
    """ This defines the class square"""
    def __init__(self, size=0):
        """
        initialization
        Args:
            size(int): the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        """area is a method that calcualtes the area of
        a sqaure given the size of the square"""
        return (self._Square__size * self._Square__size)
