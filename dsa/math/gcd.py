"""
greatest common divisor

Links:
    https://en.wikipedia.org/wiki/Greatest_common_divisor
"""


def gcd(num1: int, num2: int) -> int:
    """Computes the greatest common divisor of integers a and b using
    Euclid's Algorithm.
    """
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def test():
    """run test cases"""
    assert gcd(8, 12) == 4
    assert gcd(54, 24) == 6
