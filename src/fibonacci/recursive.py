"""
Classic recursive implementation of the fibonacci function, where recursive_fibonacci(i)
returns the i-th element of the sequence.
"""

def recursive_fibonacci(i):
    """
    time: (2^n)
        more precisely O((1+sqrt(5))/2)^n)
    space: O(n)
        note that one recursive is fully resolved before the other begins
    """
    if i == 0:
        return 0
    if i == 1:
        return 1
    return recursive_fibonacci(i - 1) + recursive_fibonacci(i - 2)
