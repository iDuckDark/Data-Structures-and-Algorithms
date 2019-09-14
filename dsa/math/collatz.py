"""
Collatz conjecture

References:
- https://en.wikipedia.org/wiki/Collatz_conjecture
"""


def collatz(number):
    """iterative"""
    result = [number]
    while number != 1:
        if number % 2 == 0:
            number //= 2
        elif number % 2 == 1:
            number = 3 * number + 1
        result.append(number)
    return result


def test():
    """test"""
    test_cases = ((12, [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]),)
    for arg, result in test_cases:
        assert collatz(arg) == result


if __name__ == "__main__":
    test()
