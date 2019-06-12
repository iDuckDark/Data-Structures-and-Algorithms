"""Linked list node to be imported"""


class Node:
    """Linked list node class"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data
