"""
functions for converting to and from roman numerals
"""


def int_to_roman(num: int) -> str:
    """convert integer to roman numeral"""
    num_map = (
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    )

    roman = ""
    while num > 0:
        for i, roman in num_map:
            while num >= i:
                roman += roman
                num -= i
    return roman


def roman_to_int(roman):
    """convert roman numeral to integer"""
    num_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": -2,
        "IX": -2,
        "XL": -20,
        "XC": -20,
        "CD": -200,
        "CM": -200,
    }
    return sum(roman.count(key) * num_map[key] for key in num_map)


def test():
    """run test cases"""
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4


if __name__ == "__main__":
    test()
