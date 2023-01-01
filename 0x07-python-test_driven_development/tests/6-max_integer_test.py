#!/usr/bin/python3
""" unitest for max_int """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test """
    def test_integers(self):
        """ test """
        test_list = [0, 1, 2, 3, 4, 5]
        self.assertEqual(5, max_integer(test_list))

    def test_negative_integer(self):
        """ test """
        test_list = [-2, -3, -5, -1, 0]
        self.assertEqual(0, max_integer(test_list))

    def test_empty_list(self):
        """ test """
        test_list = [1, "hola"]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_tupla(self):
        """ test """
        test_list = (1, 2)
        self.asserEqual(2, max_integer(test_list))

    def test_float(self):
        """ test """
        test_list = [2.5, 4.8]
        self.assertEqual(2.5, max_integer(test_list))

    def test_one_element(self):
        """ test """
        test_list = [1]
        self.assertEqual(1, max_integer(test_list))

    def test_max_at_the_beginning(self):
        """ test """
        test_list = [4, 2]
        self.assertEqual(4, max_integer(test_list))

if __name__ == '__main__':
    unitest.main()
