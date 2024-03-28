#!/usr/bin/python3
def no_c(my_string):
    updated_string = ''
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            updated_string += letter
    return updated_string
