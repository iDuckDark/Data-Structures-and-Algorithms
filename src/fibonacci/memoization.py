"""
In the traditional recursive implementation, we would redo the same calculations
(to get the value of previous elements in the sequence) multiple times. Memoization
allows those values to be stored, removing the need to redo those calculations.
"""


def memoize(fib_function):
    """
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
