#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    for i in range(len(my_list)):
        if my_list(i) < 0:
            return my_list
        else:
            del my_list[i]
