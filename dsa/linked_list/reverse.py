"""
Reverse a linked list
"""


def reverse(head):
    """Reverse a linked list in one pass
    time: O(n)
    """
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev
