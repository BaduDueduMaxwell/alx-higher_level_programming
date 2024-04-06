#!/usr/bin/python3
# 100-singly_linked_list.py by kode
""""Represents a node of a singly linked list"""


class Node:
    """Represents a node of singly linked list"""
    def __init__(self, data, next_node = None):
        """
        Initializes a new Node object.

        Args:
            data (int): The data value stored in the node.
            next_node (Node, optional): A reference to the next node in the list. Defaults to None.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not (next_node is None or isinstance(next_node, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node
        
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Represents a singly linked list."""
    def __init__(self, value=0):
        self.__head = None

    def __str__(self):
        current_node = self.__head
        output = ""
        while current_node is not None:
            output += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return output.rstrip()

    def sorted_insert(self, value):
        new_node = Node(value)
        current = self.__head
        prev = None

        while current and current.data < value:
            prev = current
            current = current.next_node

        if not prev:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new_node.next_node = current
            prev.next_node = new_node
