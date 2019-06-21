"""test linked list alogrithms"""
from dsa.linked_list import add_linked_numbers
from dsa.linked_list import Node


def test_add_linked_numbers():
    """test sorting algorithms"""
    test_cases = (
        (Node([1, 2, 3]), Node([2, 3, 4]), 357),  # 321 + 432 = 753
        (Node([2, 4, 3]), Node([5, 6, 4]), 708),  # 342 + 465 = 807
        (Node(0), Node(0), 0),  # 0 + 0 = 0
    )

    for *args, expected in test_cases:
        assert str(add_linked_numbers(*args)) == str(expected)
