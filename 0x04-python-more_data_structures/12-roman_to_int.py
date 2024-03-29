#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return None

    integer_value = 0
    for char in roman_string:
        if char == 'I':
            integer_value += 1
        elif char == 'V':
            integer_value += 5
        elif char == 'X':
            integer_value += 10
        elif char == 'L':
            integer_value += 50
        elif char == 'C':
            integer_value += 100
        elif char == 'D':
            integer_value += 500
        elif char == 'M':
            integer_value += 1000
        elif char == 'I' and roman_string[roman_string.index(char) + 1] in 'VX':
            integer_value += (roman_string[roman_string.index(char) + 1] in 'V' and 5 or 10) - 1
            continue
    return integer_value
