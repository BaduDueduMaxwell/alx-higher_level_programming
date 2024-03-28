#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    for element in my_list:
        if element in new_list:
            continue
        new_list.append(element)
    addition = sum(new_list)
    return addition
