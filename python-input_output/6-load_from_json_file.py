#!/usr/bin/python3
""" define a function that return object fro JSON file"""

import json


def load_from_json_file(filename):
    """ return object from JSON file"""
    with open(filename, 'w') as x:
        return json.load(x)
