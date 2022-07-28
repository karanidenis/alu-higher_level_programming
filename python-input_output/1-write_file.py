#!/usr/bin/python3
""" counting number of characters in a file"""


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as text:
        return text.read()

