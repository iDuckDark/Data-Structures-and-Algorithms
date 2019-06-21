"""
https://leetcode.com/problems/find-peak-element/

Given an array of integers, find the index of a peak element in it. An array element is a
peak if it is greater than or equal to its neighbors.
[10, 20, 30, 40, 50] -> 4
[1,2,1,3,5,6,4] -> 1 or 5
[1,2,3,1] -> 2
"""


def find_peak(arr):
    """
    find peak using modified binary search
    time: O(lg(n))
    space: O(1)
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == len(arr) - 1 or arr[mid] > arr[mid + 1]:
            high = mid - 1
        else:
            low = mid + 1
    return low
