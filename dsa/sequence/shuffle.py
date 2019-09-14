"""
Generate a random permutation of a finite sequence
Shuffle an array
"""
import random


def shuffle_std(seq):
    """Shuffle an array using the standard library in-place"""
    random.shuffle(seq)


def shuffle_fy(seq):
    """
    Fisher-Yates shuffle
    generates a random permutation of a finite sequence
    in-place
    time: O(n)
    space: O(1)
    References:
    https://en.wikipedia.org/wiki/Fisher–Yates_shuffle

    Args:
        seq (sequence): sequence to be shuffled
    Returns:
        (sequence): shuffled list
    """
    for i, elem in enumerate(seq):
        rand_idx = random.randrange(i, len(seq))
        seq[i], seq[rand_idx] = seq[rand_idx], elem
    return seq
