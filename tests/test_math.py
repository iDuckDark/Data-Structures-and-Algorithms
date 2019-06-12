"""test math alogrithms"""
# from dsa.math import class_memoization_fibonacci
from dsa.math import fibonacci_closed
from dsa.math import fibonacci_iterative
from dsa.math import fibonacci_memoized
from dsa.math import fibonacci_recursive


def test_fibonacci():
    """test fibonacci algorithms"""
    test_cases = ((0, 0), (1, 1), (7, 13), (10, 55))

    for args, expected in test_cases:
        # assert class_memoization_fibonacci(args) == expected
        assert fibonacci_closed(args) == expected
        assert fibonacci_iterative(args) == expected
        assert fibonacci_memoized(args) == expected
        assert fibonacci_recursive(args) == expected
