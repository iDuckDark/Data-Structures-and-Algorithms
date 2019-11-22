"""
Quick sort
Links:
    https://en.wikipedia.org/wiki/Quicksort
"""


def quicksort_recursive(arr):
    """
    Quick sort recursive
    Given indexable and slicable iterable, return a sorted list
    """
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    below = [i for i in arr[1:] if i < pivot]
    above = [i for i in arr[1:] if i >= pivot]
    return quicksort_recursive(below) + [pivot] + quicksort_recursive(above)
