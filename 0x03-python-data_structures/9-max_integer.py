#!/usr/bin/python3
def max_integer(my_list[]):

    if my_list:
        highest_num = my_list[0]
        for num in my_list:
            if num > highest_num:
                highest_num = num
        return highest_num
    else:
        return None
