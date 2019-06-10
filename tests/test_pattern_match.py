"""test pattern matching alogrithms"""
from src.pattern_match import boyer_moore
from src.pattern_match import knuth_morris_pratt


def test_pattern_match():
    """test pattern matching algorithms"""
    test_cases = (
        ("ABBCBBD", "BC", [2]),
        ("ABBCBEBCBD", "BC", [2, 6]),
        ("BCBCBC", "BC", [0, 2, 4]),
        ("BCBCBCBCBCCBBCBCBCBCBCCBBCBCBCBCBCCB", "BCBCBCBCBCCB", [0, 12, 24]),
        ("AA", "ZZ", []),
    )

    for *args, expected in test_cases:
        assert list(boyer_moore(*args)) == expected
        assert list(knuth_morris_pratt(*args)) == expected
