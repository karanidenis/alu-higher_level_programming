#!/usr/bin/python3
""" defines a function that returns python
data structure from Json representation """

import json


def from_json_string(my_str):
    """ returns python representation"""
    return json.loads(my_str)
