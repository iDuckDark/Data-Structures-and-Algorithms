"""greatest common divisor"""


def gcd(num1, num2):
    """Computes the greatest common divisor of integers a and b using
    Euclid's Algorithm.
    """
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
