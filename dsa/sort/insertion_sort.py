"""
On each loop iteration, insertion sort removes one element from the array. It
then finds the location where that element belongs within another sorted
array and inserts it there. It repeats this process until no input elements
remain.
"""


def insertion_sort(arr):
    """
    insertion sort using swap
    time: O(n^2)
    space: O(1)
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def insertion_sort_optimized(arr):
    """
    a slightly faster version that moves A[i] to its position in one go and
    only performs one assignment in the inner loop body
    time: O(n^2)
    space: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
