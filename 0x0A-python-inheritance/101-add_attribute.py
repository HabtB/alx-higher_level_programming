#!/usr/bin/python3
""" Contains a function 'add_attribute' """


def add_attribute(obj, attribute, value):
    """ This method adds a new attribute to an object """

    if '__dict__' not in dir(obj):
        raise TypeError("can't add a new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    if '__setattr__' in dir(obj):
        setattr(obj, attribute, value)
