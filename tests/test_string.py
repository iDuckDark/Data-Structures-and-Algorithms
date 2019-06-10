"""test string alogrithms"""
from src.string import common_prefix
from src.string import longest_substring


def test_common_prefix():
    """test common prefix"""
    test_cases = (
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["aaa", "aa"], "aa"),
        ([], ""),
        (["a"], "a"),
        ([""], ""),
    )

    for args, expected in test_cases:
        assert common_prefix(args) == expected


def test_longest_substring():
    """test longest substring"""
    test_cases = (
        ("", 0),
        ("a", 1),
        ("ab", 2),
        ("aba", 2),
        ("bacdea", 5),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    )

    for args, expected in test_cases:
        assert longest_substring(args) == expected
