"""test sorting alogrithms"""
from dsa.sort import insertion_sort
from dsa.sort import insertion_sort_optimized
from dsa.sort import merge_sort
from dsa.sort import selection_sort


def test_sort():
    """test sorting algorithms"""
    test_cases = (
        ([0], [0]),
        ([2, 1], [1, 2]),
        ([1, 5, 65, 23, 57, 1232], [1, 5, 23, 57, 65, 1232]),
    )

    for args, expected in test_cases:
        assert insertion_sort(args) == expected
        assert insertion_sort_optimized(args) == expected
        assert selection_sort(args) == expected
        assert merge_sort(args) == expected
