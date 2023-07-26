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
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """
    A class representing a singly linked list in python
    """
    def __init__(self):
        self._head = None
        self._element = []

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            self._head = new_node
            current._next__node = self._head
        self._element.append(self._head)

    def __str__(self):
        return self._element.sort(key=self._head.data)
