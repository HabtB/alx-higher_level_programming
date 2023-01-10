#!/usr/bin/python3
""" Contains the clase BaseGeometry and Sclass Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A representation of a rectangle """
    def __init__(self, width, height):
        """ instantiation of a rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Calculates the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
