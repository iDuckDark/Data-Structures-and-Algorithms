"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
from .node import Node


def add_linked_numbers(node_a: Node, node_b: Node) -> Node:
    """
    Add two numbers stored in reverse order
    time: O(n)
    space: O(n)
    """
    current = head = Node(0)
    _sum = 0
    while node_a or node_b:
        if node_a:
            _sum += node_a.val
            node_a = node_a.next
        if node_b:
            _sum += node_b.val
            node_b = node_b.next
        current.next = Node(_sum % 10)
        current = current.next

    if _sum // 10:  # is there a carry at the end?
        current.next = Node(1)
    return head.next


def int_to_list(number: int) -> Node:
    """
    convert a positive integer into a (reversed) linked list.
    112 -> 2 -> 1 -> 1
    """
    head = Node(0)
    current = head
    remainder = number % 10
    quotient = number // 10

    while quotient != 0:
        current.next = Node(remainder)
        current = current.next
        remainder = quotient % 10
        quotient //= 10
    current.next = Node(remainder)
    return head.next


def list_to_int(lst: Node) -> int:
    """
    convert a non-negative number list into a string.
    TODO: use numbers instead of strings
    """
    result = ""
    while lst:
        result += str(lst.val)
        lst = lst.next
    return int(result)
