"""
Given a list on non-negative integers, find the max sum without using adjacent
numbers.

References:
- https://leetcode.com/problems/house-robber/
"""
from typing import List


def max_sum(nums: List[int]) -> int:
    """
    Observe the next two elements and select the one that maximizes the sum.
    Time: O(n)
    """
    prev1, prev2 = 0, 0
    for num in nums:
        prev1, prev2 = max(prev2 + num, prev1), prev1

    return prev1


def test():
    """run test cases"""
    test_cases = (
        ([], 0),
        ([1], 1),
        ([1, 2, 3, 1], 4),
        ([4, 2, 3, 4], 8),
        ([2, 7, 9, 3, 1], 12),
    )
    for arg, expected in test_cases:
        assert max_sum(arg) == expected


if __name__ == "__main__":
    test()
