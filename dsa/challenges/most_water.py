"""
References:
- https://leetcode.com/problems/container-with-most-water/
"""
from typing import List


def solve_naive(heights: List[int]) -> int:
    """
    naive solution
    Time: O(n^2)
    """
    max_vol = 0
    for i, start in enumerate(heights):
        for j, end in enumerate(heights[i + 1 :], i + 1):
            max_vol = max(min(start, end) * (j - i), max_vol)
    return max_vol


def solve(heights: List[int]) -> int:
    """
    work from both ends
    Time: O(n)
    """
    max_vol = 0
    i = 0
    j = len(heights) - 1
    while i < j:
        max_vol = max(min(heights[i], heights[j]) * (j - i), max_vol)
        if heights[i] > heights[j]:
            j -= 1
        else:
            i += 1
    return max_vol


def test():
    """run test cases"""
    test_cases = (
        ([], 0),
        ([1, 1], 1),
        ([5, 2, 4], 8),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    )
    for arg, expected in test_cases:
        assert solve_naive(arg) == expected
        assert solve(arg) == expected


if __name__ == "__main__":
    test()
