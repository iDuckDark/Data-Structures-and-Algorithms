"""
Implement random shuffle based on a random generator between [0, 1)
"""

import math
import random


def shuffle(arr):
    """
    time: O(n)
    space: O(1)
    """
    for i, elem in enumerate(arr):
        # Swaps current element with another element at random.
        other = math.floor(random.random() * (len(arr) - i)) + i
        # Note: we only consider swapping with elements in the array that are after the
        # current index (this ensures true randomness).
        arr[i], arr[other] = arr[other], elem
    return arr
