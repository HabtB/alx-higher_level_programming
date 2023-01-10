#!/usr/bin/python3
""" A module that contains "MyInt" class """


def MyInt(int):
    """ Defines MyInt class reversing '==' and '!=' """

    def __new__(cls, value):
        return new.__new__(cls, int)        

    def __eq__(self, other):
        """ inverts the equal method """
        return int(str(self)) != other

    def __ne__(self, other):
        """ inverts the not-equal method """
        return int(str(self)) == other
