#!/usr/bin/python3
""" module class with private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None):
"""
import json
import csv
import os.path


class Base:
    """ class base with private attributes and constructors """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialise instance
        :param id:
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dicts):
        """ changing lists to json strings"""
        if list_dicts is None or list_dicts == "[]":
            return "[]"
        return json.dumps(list_dicts)

    @classmethod
    def save_to_file(cls, list_objs):
        """saving objects in a file"""
        filename = "{}.json".format(cls.__name__)
        list_dict = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dict())

        lists = cls.to_json_string(list_dict)
        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """changing from json"""
        if not json_string:
            return []
        return json.loads(json_string)


if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    # print(Base(12).__nb_instances) #private instance

    b1 = Base(None)  # None id
    b2 = Base(12)
    b3 = Base(None)
    print(b1.id, b3.id - 1)

    b = Base(12)  # unique id
    b.id = 15
    print(b.id)

    b = Base("hello")  # string id
    print(b.id)

    b = Base(2.2)  # float id
    print(b.id)

    b = Base(complex(5))  # complex id
    print(b.id)

    b = Base({"a": 1, "b": 2})  # dict id
    print(b.id)

    b = Base([1, 2, 3])  # list id
    print(b.id)

    b = Base((1, 2, 3))  # tuple id
    print(b.id)

    b = Base({1, 2, 3})  # set id
    print(b.id)

    b = Base(range(5))  # range id
    print(b.id)

    b = Base(b'python')  # bytes id
    print(b.id)

    b = Base(float('nan'))  # nan id
    print(b.id)
