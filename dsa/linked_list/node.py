"""Linked list node to be imported"""
from typing import Iterable


class Node:
    """Linked list node class"""

    def __init__(self, data):
        if isinstance(data, Iterable):
            sentinel = self
            for element in data:
                prev = sentinel
                sentinel.data = element
                sentinel.next = Node(None)
                sentinel = sentinel.next
            prev.next = None
        else:
            self.data = data
            self.next = None

    def __iter__(self):
        current = self
        while current:
            yield current
            current = current.next

    def __str__(self):
        return "".join(str(x.data) for x in self)

    def __eq__(self, other):
        return self.data == other.data

    def display(self):
        """concatenate all elements"""
        return " -> ".join(str(x.data) for x in self)
