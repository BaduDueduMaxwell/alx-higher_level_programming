#!/usr/bin/python3

def element_at(my_list, idx):
    for number in idx:
        if idx < 0 or idx >= len(my_list):
            return None
        else:
            return my_list[idx]
