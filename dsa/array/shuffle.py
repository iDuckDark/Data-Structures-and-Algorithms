"""
Generate a random permutation of a finite sequence
Shuffle an array
"""
import random


def shuffle_std(arr):
    """Shuffle an array using the standard library in-place"""
    random.shuffle(arr)


def shuffle_fy(arr):
    """
    Fisher-Yates shuffle
    generates a random permutation of a finite sequence
    in-place

    Time: O(n)
    Space: O(1)
    Links:
        https://en.wikipedia.org/wiki/Fisher–Yates_shuffle

    Args:
        seq (sequence): sequence to be shuffled
    Returns:
        (sequence): shuffled list
    """
    for i, elem in enumerate(arr):
        rand_idx = random.randrange(i, len(arr))
        arr[i], arr[rand_idx] = arr[rand_idx], elem
    return arr
