#!/usr/bin/python3

for num1 in range(0, 8):
    for num2 in range(0, 10):
        if (num1 < num2 and num1 != num2 ):
            print("{:d}{:d}".format(num1, num2), end=", ")
print("{:02d}".format(89))
