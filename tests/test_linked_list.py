"""test linked list alogrithms"""
from dsa.linked_list import add_linked_numbers
from dsa.linked_list import int_to_list
from dsa.linked_list import list_to_int


def test_add_linked_numbers():
    """test sorting algorithms"""
    test_cases = (
        (int_to_list(342), int_to_list(465), 807),
        (int_to_list(0), int_to_list(0), 0),
    )

    for *args, expected in test_cases:
        assert list_to_int(add_linked_numbers(*args)) == expected
