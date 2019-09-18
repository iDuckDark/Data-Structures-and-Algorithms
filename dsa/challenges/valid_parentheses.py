"""check if parentheses are balanced"""


def is_valid(string: str) -> bool:
    """is valid"""
    stack = []
    braces = {")": "(", "]": "[", "}": "{"}
    for char in string:
        if char in braces.values():
            stack.append(char)
        elif not stack or stack.pop() != braces[char]:
            return False
    return not stack


def test():
    """test"""
    test_cases = (
        ("", True),
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    )
    for arg, expected in test_cases:
        assert is_valid(arg) == expected


if __name__ == "__main__":
    test()
