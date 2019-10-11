"""
Binary search

References:
- https://en.wikipedia.org/wiki/Binary_search_algorithm
"""


def binary_search(arr, target):
    """
    arr must be sorted, O(nlogn)
    given an array and a target value, return the index
    returns -1 if the target is not present

    Best case: O(1)
    Worst case: O(log n)
    Worst case space: O(1)
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return mid
    return -1

    # replace with this line for nearest
    # return low if arr[low] - target < target - arr[high] else high


def binary_search_recur(arr, low, high, num):
    """
    recursive variant of binary search
    """
    if low > high:  # error case
        return -1
    mid = (low + high) // 2
    if num < arr[mid]:
        return binary_search_recur(arr, low, mid - 1, num)
    if num > arr[mid]:
        return binary_search_recur(arr, mid + 1, high, num)
    return mid


def test():
    """run test cases"""
    tests = (
        ([1, 2, 4, 7, 9, 11], 5, -1),
        ([3, 5, 7, 8, 9, 10], 3, 0),
        ([1, 5, 8, 10], 0, -1),
        ([1, 5, 8, 10], 5, 1),
    )
    for *args, result in tests:
        assert binary_search(*args) == result


if __name__ == "__main__":
    test()
