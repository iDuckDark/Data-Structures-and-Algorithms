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
    assert is_valid("()")
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    assert not is_valid("([)]")
    assert is_valid("{[]}")
    assert is_valid("")


if __name__ == "__main__":
    test()
