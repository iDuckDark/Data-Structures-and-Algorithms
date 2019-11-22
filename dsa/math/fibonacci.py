"""
The Fibonacci sequence is defined as a recurrence relation.
fn+1 = fn + fn-1, with f(0) = 1, and f(1) = 1

Links:
    https://en.wikipedia.org/wiki/Fibonacci_number
"""
import functools
import math


def fibonacci_recursive(n):
    """Recursive implementation of the fibonacci function

    time: (2^n)
        more precisely O((1+sqrt(5))/2)^n)
    space: O(n)
        note that one recursive is fully resolved before the other begins
    """
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """Iterative implementation of the fibonacci function

    Time: O(n)
    """
    last, curr = 0, 1
    for _ in range(n):
        last, curr = curr, last + curr
    return last


@functools.lru_cache()
def fibonacci_memoized(n):
    """
    Memoization refers to remembering results of method calls based on the
    method inputs and then returning the remembered result rather than
    computing the result again.

    time: O(n)
    space O(n)
    """
    if n < 2:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


def fibonacci_closed(n):
    """
    We can calculate a closed form representation, as taught in introductory
    discrete structure courses.
    Approach: http://discrete.openmathbooks.org/dmoi2/sec_recurrence.html

    time: O(1)
    space: O(1)
    """
    golden_ratio = (1 + math.sqrt(5)) / 2
    return round(golden_ratio ** n / math.sqrt(5))


def test():
    """run test cases"""
    test_cases = ((0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (12, 144))

    for arg, expected in test_cases:
        assert fibonacci_iterative(arg) == expected


if __name__ == "__main__":
    test()
