#!/usr/bin/python3
""" define a function that writes an Object to a text file,
using a JSON representation:
"""

import json


def save_to_json_file(my_obj, filename):
    """ write an object to a text file using JSON"""
    with open(filename, 'w') as b:
        json.dump(my_obj, b)
