#!/usr/bin/python3
""" inserting lines to text file"""


def append_after(filename="", search_string="", new_string=""):
    """
    :param filename: file name
    :param search_string: insert line where there's search string
    :param new_string:
    """
    with open(filename, 'r+') as b:
        lines = b.readlines()
        lin = []
        for line in range(len(lines)):
            lin.append(lines[line])
            if search_string in lines:
                lin.append(new_string)

        lin.write("lin")
