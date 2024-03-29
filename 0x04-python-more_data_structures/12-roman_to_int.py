#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
                 'I': 1}
    integer_value = 0
    for roman in reversed(roman_string):
        roman_key = roman_map[roman]
        integer_value += roman_key if integer_value < roman_key * 5 \
            else -roman_key
    return integer_value
