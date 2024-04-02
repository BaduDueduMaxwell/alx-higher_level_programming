#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if str(value).isdigit():
            print("{:d}".format(value))
            return True
    except:
        return False
