"""Linked list node to be imported"""


class Node:
    """Linked list node class"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        out = []
        node = self
        while node:
            out.append(str(node.data))
            node = node.next

        return " -> ".join(out)

    def __eq__(self, other):
        return self.data == other.data
