#!/usr/bin/env python3

islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("a") else "upper"))
print("A is {}".format("lower" if islower("a") else "upper"))
print("3 is {}".format("lower" if islower("a") else "upper"))
print("g is {}".format("lower" if islower("a") else "upper"))
