#!/usr/bin/python3
"""This module appends a string at the end of a text file and returns num of chaacters"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        content = file.write(text)
    return len(text)
