"""
Alternate sum
"""
from typing import List


def solve(arr: List[int]) -> int:
    """
    alternate sum
    Time: O(n)
    """
    return sum(x if i % 2 == 0 else -x for i, x in enumerate(arr))


def test():
    """run test cases"""
    test_cases = (([], 0), ([1], 1), ([5, 2, 1, 3, 4], 5), ([1, 2, 3, 4, 5], 3))

    for arg, expected in test_cases:
        assert solve(arg) == expected


if __name__ == "__main__":
    test()
