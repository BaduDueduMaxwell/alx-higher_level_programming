#!/usr/bin/python3
"""This module defines a text file-reading function"""


def read_file(filename=""):
    """Reads the contents of a text file (UTF8) and prints it"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print(content)
