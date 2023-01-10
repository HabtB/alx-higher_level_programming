#!/usr/bin/python3
""" Contains the function "inherits_from.py" """


def inhertis_from(obj, a_class):
    """ This functions returns True if object is instance of
    inherited from class otherwise return False"""

    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
