#!/usr/bin/python3
""" Contains the clase BaseGeometry and Sclass Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A representation of a square """
    def __init__(self, size):
        """ instantiation of a rectangle """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """ calculates the area of a square """
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
