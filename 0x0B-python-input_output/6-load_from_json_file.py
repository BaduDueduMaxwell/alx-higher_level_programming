#!/usr/bin/python3
"""This module creates an obj from a JSON file"""
import json


def load_from_json_file(filename):
    """function that creates an object from a JSON file"""
    with open(filename, 'r') as file:
        return json.load(file)
