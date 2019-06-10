"""
Classic iterative implementation of the fibonacci function, where recursive_fibonacci(i)
returns the i-th element of the sequence.
"""

def iterative_fibonacci(i):
    """
    time: O(n)
    space: O(n)
    """
    if i == 0:
        return 0
    last = 0
    current = 1
    for _ in range(1, i):
        temp = current + last
        last = current
        current = temp
    return current
