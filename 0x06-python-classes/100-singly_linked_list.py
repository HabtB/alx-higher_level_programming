#!/bin/bahs
""" singly linked list in python """


class Node:
    """ defines the Node """

    def __init__(self, data, next_node=None):
        """ initializes the node
        Args:
            data(int): the data stored in the node
            next_node: indicates the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets the data of the node"""
        return self.__data

    @property
    def next_node(self):
        """ gets the next_node """
        return self.__next_node

    @data.setter
    def data(self, value):
        """ sets the data of the node """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.linked_list = []

    def sorted_insert(self, value):
        new_node = Node(value)
        new_node.next_node = self.__head
        self.__head = new_node
        self.linked_list = []
        aux = Node(self.__head.data, self.__head.next_node)

        while aux is not None:
            self.linked_list.append(aux.data)
            aux = aux.next_node
        self.linked_list.sort()

    def __str__(self):
        return "\n".join(list(map(str, self.linked_list)))
