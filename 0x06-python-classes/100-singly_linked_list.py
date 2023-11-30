#!/usr/bin/python3
"""
Author: Mire
Description: Implementation of linked list in python
"""
class Node:
    """
    A class representing a node containing a data and the next node
    """
    def __init__(self, data, next_node=None):
        self._node__data = data
        self._next__node = next_node

    @property
    def data(self):
        return self._node__data

    @data.setter
    def data(self, value):
        if type(value) == int:
            self._node__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self._next__node

    @next_node.setter
    def next_node(self, value):
        if type(value) == Node:
            self._next__node = value
        else:
            print(type(value))
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """
    A class representing a singly linked list in python
    """
    def __init__(self):
        self._head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            while current.next_node:
                if current.next_node.data >= new_node.data:
                    break
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        current = self._head
        while current:
            print(current.data)
            current = current.next_node
