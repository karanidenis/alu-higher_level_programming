#!/usr/bin/python3
""" add, load and ve arguments"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as b:
        import json
        a = json.dumps(my_obj)
        b.write(a)
