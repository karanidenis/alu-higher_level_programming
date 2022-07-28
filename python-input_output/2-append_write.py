#!/usr/bin/python3
""" append and counting number of characters in a file"""


def write_file(filename="", text=""):
    """
     function creates a new file or appends current one
     and counts number of characters added
     Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """

    with open(filename, mode='a', encoding='utf-8') as a_text:

        return a_text.write(text)
