"""
The Fibonacci sequence is defined as a recurrence relation.
fn+1 = fn + fn-1, with f(0) = 1, and f(1) = 1
"""

import math


def recursive_fibonacci(i):
    """ Classic recursive implementation of the fibonacci function, where
    recursive_fibonacci(i) returns the i-th element of the sequence.

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


def iterative_fibonacci(i):
    """ Classic iterative implementation of the fibonacci function, where
    recursive_fibonacci(i) returns the i-th element of the sequence.

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


def memoize(fib_function):
    """ In the traditional recursive implementation, we would redo the same calculations
    (to get the value of previous elements in the sequence) multiple times. Memoization
    allows those values to be stored, removing the need to redo those calculations.

    Avoid redoing previous calculations, by storing their return values. Checks to see
    a calculation has been done in the past. If so, return the cached value.
    """
    memory = {}

    # A function which wraps around the original function and checks whether a past
    # calculation has already been performed.
    def wrapper(i):
        if i not in memory:
            memory[i] = fib_function(i)
        return memory[i]

    return wrapper


@memoize
def function_memoization_fibonacci(i):
    """ The @memoize key word is called a function decorator.
    By having the decorator, we are essentially doing fibonacci = memoize(fibonacci).
    time: O(n)
    space O(n)
    """
    if i == 0:
        return 0
    if i == 1:
        return 1
    return function_memoization_fibonacci(i - 1) + function_memoization_fibonacci(i - 2)


class Memoize:
    """
    We can also encapsulate the cached value inside a class.
    """

    def __init__(self, fib_function):
        self.function = fib_function
        self.memory = {}

    def __call__(self, *args):
        if args not in self.memory:
            self.memory[args] = self.function(*args)
        return self.memory[args]


@Memoize
def class_memoization_fibonacci(i):
    """
    time: O(n)
    space O(n)
    """
    if i == 0:
        return 0
    if i == 1:
        return 1
    return class_memoization_fibonacci(i - 1) + class_memoization_fibonacci(i - 2)


def explicit_fibonacci(i):
    """
     We can calculate a close form representation, as taught in introductory
     discrete structure courses. 

     Approach: http://discrete.openmathbooks.org/dmoi2/sec_recurrence.html

     time: O(1)
     space: O(1)
     """
    a = 1 / math.sqrt(5) * ((1 + math.sqrt(5)) / 2) ** i
    b = 1 / math.sqrt(5) * ((1 - math.sqrt(5)) / 2) ** i
    # Note: (1 + sqrt(5)) / 2 is the golden ratio!
    return round(a - b)
