#!/usr/bin/python3

def uppercase(str):
    for char in str:
        newchar = char
        if (ord(char) >= 97 and ord(char) <= 122):
            newchar = chr(ord(char) - 32)
        print("{:s}".format(newchar), end='')
    print("")
