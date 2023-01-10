#!/usr/bin/python3
""" Contains a module that contains a class MyList that
inhertis from list - object
"""


class MyList(list):
    """ inherts from list """
    def print_sorted(self):
        """ prints the list, sorted in ascending order"""
        print(sorted(self))
