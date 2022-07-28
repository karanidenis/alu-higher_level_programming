#!/usr/bin/python3
""" function that prints output as stdout"""


def read_file(filename=""):
    """
    read file and print in stdout
    :param filename:
    """

    with open(filename) as f:
        s = f.read()
        print(s, end="")
