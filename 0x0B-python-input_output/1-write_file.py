#!/usr/bin/python3
"""This module defines a text file-writing function"""


def write_file(filename="", text=""):
    """Writes the contents of a text file (UTF8) and prints it"""
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters
