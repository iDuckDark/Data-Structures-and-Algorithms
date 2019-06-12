"""
Given an array of values, determine whether a subset of the array adds up to a target
sum.

This problem is NP-Complete. However, it can be solved in pseudo-polynomial time, as
shown below. Pseudo-polynomial means that the complexity is determined by the actual
value of the input (in this case, the target number) and not the length of the input.

Even if there are few elements in the array, if the target value is large, this solution
is infeasible.
"""

def _preprocess(arr, target):
    """
    Initializes a table which will store subset sums obtainable by the elements that
    have been previous considered.
    """
    result = [[False] * (target + 1) for _ in range(len(arr) + 1)]
    result[0][0] = True
    # Go through each element in the array, and update the table with all the new
    # values that can now be attained through its inclusion.
    for i, _ in enumerate(arr):
        previous = result[i]
        current = result[i + 1]
        for value in range(target + 1):
            # A dynamic value is one that can obtained by adding a previously attainable
            # value to the current value.
            dynamic_value = value - arr[i]
            if previous[value] or (dynamic_value >= 0 and previous[dynamic_value]):
                current[value] = True
    return result


def dynamic_subset_sum(arr, target):
    """
    time: O(nm)
    space: O(nm)
        where m == target and n is the length of the array
    """
    arr.sort()
    table = _preprocess(arr, target)
    # The target value must be true on the final row, if it is attainable.
    if not table[-1][-1]:
        return False
    result = []
    value = target
    row = len(arr)
    # Gather the values that add up to the sum. If the desired value is True on the
    # current row, but unattainable in the previous, then the element associated with
    # the current row must be necessary for attaining the target sum.
    while row > 0:
        if not table[row - 1][value]:
            result.append(arr[row - 1])
            value -= arr[row - 1]
        row -= 1
    return result
