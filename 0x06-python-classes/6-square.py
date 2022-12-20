#!/usr/bin/python3
""" Class Square: defines a class with an instant variable size """


class Square:
    """ This defines the class square
    Attributes:
        __size (int): size of the square
        __position (tuple): position of the sqaure
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialization
        Args:
            size(int): the size of the square
            position(tuple): coordiantes of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """area is a method that calcualtes the area of
        a sqaure given the size of the square
        Returns:
            The area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ Get the current size of the square
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ Set the current size of the square
        Args:
            size(int): size of the size of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def my_print(self):
        """ This prints the square
        Returns:
            None
        """

        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for m in range(self.__position[0])]), end="")
            print("".join(["#" for n in range(self.__size)]))

    @property
    def position(self):
        """retrieves the position(tuple of the square)
        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the position of the square
        Args:
            value(tuple): position of the square
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
