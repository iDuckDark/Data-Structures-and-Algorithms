"""test array alogrithms"""
from dsa.sequence import find_peak
from dsa.sequence import two_sum_dict
from dsa.sequence import two_sum_naive


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
