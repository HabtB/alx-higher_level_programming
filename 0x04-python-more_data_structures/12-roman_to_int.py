#!/usr/bin/python3
roman_constant = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                  "D": 500, "M": 1000}


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0

    for i, c in enumerate(roman_string):
        if roman_constrant.get(c) is None:
            return 0
        if len(roman_string) > i + 1:
            if roman_constant.get(c) < roman_string.get(roman_string[i + 1]):
                result -= roman_constant.get(c)
            else:
                result += roman_constant.get(c)
        else:
            result += roman_constant.get(c)
    return result
