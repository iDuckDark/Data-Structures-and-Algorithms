"""Linked list

Reference:
- https://en.wikipedia.org/wiki/Linked_list
- https://stackoverflow.com/a/50483259/9518712
"""


class Node:
    """linked list node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return f"Node({self.data}, {self.next})"


class LinkedList:
    """linked list"""

    def __init__(self, head: Node = None):
        self.head = head

    def is_empty(self) -> bool:
        """return whether the linked list contains no nodes"""
        return self.head is None

    def insert(self, node: Node):
        """insert node at beginning of list"""
        node.next = self.head
        self.head = node

    def append(self, node: Node):
        """
        append node to end of linked list
        O(n) time
        """
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def pop(self, index=None):
        """remove last node"""
        if self.is_empty():
            raise IndexError("pop from empty list")

        current = self.head
        previous = None

        i = 0
        while current.next is not None:
            if i == index:
                break
            previous = current
            current = current.next
            i += 1

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        return current.data

    def __contains__(self, key):
        for node in self:
            if node.data == key:
                return True
        return False

    def __iter__(self):
        sentinel = self.head
        while sentinel:
            yield sentinel
            sentinel = sentinel.next

    def __str__(self):
        return "->".join(str(node.data) for node in self)


def test():
    """run test cases"""
    lst = LinkedList(Node(3))
    lst.append(Node(5))
    lst.append(Node(6))
    assert str(lst) == "3->5->6"
    assert lst.pop() == 6
    assert str(lst) == "3->5"


if __name__ == "__main__":
    test()
