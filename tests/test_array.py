"""test array alogrithms"""
from src.array import dynamic_subset_sum
from src.array import find_peak
from src.array import two_sum_dict
from src.array import two_sum_naive


def test_two_sum():
    """test two sum"""
    test_cases = (
        ([2, 11, 7, 9], 9, (0, 2)),
        ([-3, 5, 2, 3, 8, -9], 0, (0, 3)),
        ([-3, 5, 2, 3, 8, -9], 6, None),
    )

    for *args, expected in test_cases:
        assert two_sum_dict(*args) == expected
        assert two_sum_naive(*args) == expected


def test_find_peak():
    """test find peak"""
    test_cases = (
        ([10, 20, 30, 40, 50], 4),
        ([1, 2, 3, 1], 2),
        ([1], 0),
        ([4, 3, 2, 1], 0),
    )

    for args, expected in test_cases:
        assert find_peak(args) == expected


def test_dynamic_subset_sum():
    """test dynamic subset sum"""
    test_cases = (
        (([2, 2], 4), [2, 2]),
        (([1, 2], 4), False),
        (([2, 2, 7, 11], 20), [11, 7, 2]),
        (([2, 2, 8], 7), False),
    )

    for args, expected in test_cases:
        assert dynamic_subset_sum(*args) == expected
