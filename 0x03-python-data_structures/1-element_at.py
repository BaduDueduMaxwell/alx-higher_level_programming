#!/usr/bin/python3

def element_at(my_list, idx):
    for number in idx:
        if number < 0:
            return None
    for digit in my_list:
        if digit > 0:
            return None
