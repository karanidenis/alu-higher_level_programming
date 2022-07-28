#!/usr/bin/python3
""" defines a function that returns python data structure from Json representation """

import json


def from_json_string(my_str):
    """ function that returns python representation"""
    return json.load(my_str)
