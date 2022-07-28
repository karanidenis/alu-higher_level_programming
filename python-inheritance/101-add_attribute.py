#!/usr/bin/python3
"""function that adds a new attribute if possible"""


def add_attribute(obj, attr, value):
    """
    :param obj: add object
    :param attr: name of attribute
    :param value: value of the attribute
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
