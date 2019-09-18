"""
Rob houses

References:
- https://leetcode.com/problems/house-robber/
"""

from typing import List


def rob(nums: List[int]) -> int:
    """
    O(n)
    """
    prev1, prev2 = 0, 0
    for num in nums:
        prev1, prev2 = max(prev2 + num, prev1), prev1

    return prev1


def test():
    """test"""
    test_cases = (([1, 2, 3, 1], 4), ([2, 7, 9, 3, 1], 12))
    for arg, expected in test_cases:
        assert rob(arg) == expected
