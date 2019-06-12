"""test fibonacci alogrithms"""
from src.math import class_memoization_fibonacci
from src.math import explicit_fibonacci
from src.math import function_memoization_fibonacci
from src.math import iterative_fibonacci
from src.math import recursive_fibonacci


def test_fibonacci():
    """test fibonacci algorithms"""
    test_cases = (
        (0, 0),
        (1, 1),
        (7, 13),
        (10, 55),
    )

    for args, expected in test_cases:
        assert class_memoization_fibonacci(args) == expected
        assert explicit_fibonacci(args) == expected
        assert function_memoization_fibonacci(args) == expected
        assert iterative_fibonacci(args) == expected
        assert recursive_fibonacci(args) == expected
