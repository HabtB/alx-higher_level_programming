#!/usr/bin/python3
def magic_string(magic_number=[0]):
    magic_number[0] += 1
    return (", ".join("BestSchool" for magic_number in range(magic_number[0])))
