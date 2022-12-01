#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    num = len(argv)
    if (num < 2):
        print("0 argument.")
    elif (num == 2):
        print("1 argument:")
    else:
        print("{} arguments:".format(num - 1))
    for i in range(1, num):
        print("{:d}: {}".format(i, argv[i]))
