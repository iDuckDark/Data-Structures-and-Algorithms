"""
Quick sort
References:
- https://en.wikipedia.org/wiki/Quicksort
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


def test():
    """test"""
    tests = (
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([2, 1, 3, 4], [1, 2, 3, 4]),
        ([1, 3, 2, 4], [1, 2, 3, 4]),
        ([1, 2, 4, 3], [1, 2, 3, 4]),
        ([1, 2, 4, 3], [1, 2, 3, 4]),
        ([2, 1, 1, 1], [1, 1, 1, 2]),
        ([1, 2, 1, 1], [1, 1, 1, 2]),
        ([1, 1, 2, 1], [1, 1, 1, 2]),
        ([1, 1, 1, 2], [1, 1, 1, 2]),
    )
    for arg, result in tests:
        assert quicksort_recursive(arg) == result


if __name__ == "__main__":
    test()
