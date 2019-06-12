"""
In Selection sort, we divide our input list / array into two parts: the
sublist of items already sorted and the sublist of items remaining to be
sorted that make up the rest of the list. We first find the smallest element
in the unsorted sublist and place it at the end of the sorted sublist. Thus,
we are continuously grabbing the smallest unsorted element and placing it in
sorted order in the sorted sublist. This process continues iteratively until
the list is fully sorted.
"""


def selection_sort(arr):
    """
    simple selection sort
    time: O(n^2)
    space: O(1)
    """
    for i, _ in enumerate(arr):
        min_idx = i
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[min_idx]:
                min_idx = j
        # swap the element to the end of the sorted array
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr
