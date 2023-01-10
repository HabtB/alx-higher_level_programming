#!/usr/bin/python3
""" The module contains a function that helps to
find out is an instance is in the same class"""


def is_same_class(obj, a_class):
    """ Is a function that returns True if an object
    is in the given class, otherwise False """
    if type(obj) is a_class:
        return True
    return False
