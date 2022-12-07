#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_b = {}
    for key, value in a_dictionary.items():
        dict_b[key] = value * 2
    return dict_b
