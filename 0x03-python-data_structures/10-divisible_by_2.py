#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    for multiple in range(len(my_list)):
        if multiple % 2 == 0:
            return True
        else:
            return False
