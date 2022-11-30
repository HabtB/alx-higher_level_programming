#!/usr/bin/python3

def print_last_digit(number):
    ldigit = abs(number) % 10
    print("{:d}".format(ldigit), end="")
    return ldigit
