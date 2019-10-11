"""
Base conversion

References:
- https://bradfieldcs.com/algos/stacks/converting-number-bases/
"""

SYMBOLS = "0123456789abcdefghijklmnopqrstuvwxyz"


def convert_to_base(decimal_number: int, base: int):
    """
    Args:
        decimal_number: the number to convert
        base: > 0, the base to convert to
    Returns:
        The decimal number converted to the requested base
    """
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base

    new_digits = [SYMBOLS[digit] for digit in reversed(remainder_stack)]

    return "".join(new_digits)


def test():
    """run test cases"""
    test_cases = (((25, 2), "11001"), ((25, 16), "19"))

    for args, expected in test_cases:
        assert convert_to_base(*args) == expected


if __name__ == "__main__":
    test()
