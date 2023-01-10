#!/usr/bin/python3
""" This module checks if the object is an instance of
or an instance of a class that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """ Is the function that checks if a class is an instance of
    an object or an instance of a class that inherited from the
    given class """

    return isinstance(obj, a_class)
