#!/usr/bin/python3
""" class student """

import json


class Student:
    """ define function"""


def __init__(self, first_name, last_name, age):
    """
    :param self:
    :param first_name:
    :param last_name:
    :param age:
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


def to_json(self):
    return json.dumps(self.Student.__dict__)
