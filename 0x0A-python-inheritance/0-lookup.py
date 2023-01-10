#!/usr/bin/python3
""" This module contains the lookup function """


def lookup(obj):
    """ returns a list of available attributes and
        and methods of an object
    """
    return dir(obj)
