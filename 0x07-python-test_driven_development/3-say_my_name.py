#!/usr/bin/python3
""" This module has a function that
    prints the first and last names
"""


def say_my_name(first_name, last_name=""):
    """ This function prints the first name
        and last name
        Args:
            first_name: a first name string
            last_name: a last name string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
