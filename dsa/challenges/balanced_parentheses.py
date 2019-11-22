"""
Check if parentheses in a string are balanced.

Links:
    https://bradfieldcs.com/algos/stacks/balanced-parentheses/
"""


def is_balanced(string: str) -> bool:
    """
    Args:
        string: A string consisting only of parentheses.
    Time: O(n)
    Space: O(n)
    """
    stack = []
    braces = {")": "(", "]": "[", "}": "{"}
    for char in string:
        if char in braces.values():
            stack.append(char)
        elif not stack or stack.pop() != braces[char]:
            return False
    return not stack


def test():
    """run test cases"""
    test_cases = (
        ("", True),
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("((()))", True),
        ("(()", False),
        ("())", False),
    )
    for arg, expected in test_cases:
        assert is_balanced(arg) == expected


if __name__ == "__main__":
    test()
