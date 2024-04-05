#!/usr/bin/python3
# 100-singly_linked_list.py by kode
""""defines a node of a singly linked list"""


class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

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
    def __init__(self, value=0):
        self.__head = None

    def head(self):
        return self.__head

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current_node = self.__head
        while current_node.next_node is not None and current_node.next_node.data < value:
            current_node = current_node.next_node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
