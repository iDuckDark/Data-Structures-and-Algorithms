"""
Given a linked list, remove the n-th node from the end of list and return its head.
"""


def remove_nth_from_end(head, n):
    """
    One pass
    O(n)
    """
    front = head
    current = head

    for _ in range(n):
        front = front.next
    if not front:
        return head.next

    while front:
        front = front.next
        if front:
            current = current.next

    current.next = current.next.next
    return head
