"""test fibonacci alogrithms"""
from src.fibonacci import class_memoization_fibonacci
from src.fibonacci import explicit_fibonacci
from src.fibonacci import function_memoization_fibonacci
from src.fibonacci import iterative_fibonacci
from src.fibonacci import recursive_fibonacci


def test_sort():
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
