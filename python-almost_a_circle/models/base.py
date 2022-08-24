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
        if list_dicts is None or list_dicts == 0:
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

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ serializes """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV"""
        ld = []
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        ld.append([
                            obj.id, obj.width, obj.height, obj.x, obj.y])
                    if cls.__name__ == 'Square':
                        ld.append([obj.id, obj.size, obj.x, obj.y])
            writer = csv.writer(f)
            for row in ld:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes in CSV """
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                ld = []
                reader = csv.DictReader(f)
                for row in reader:
                    for key, val in row.items():
                        row[key] = int(val)
                ld.append(row)
                return [cls.create(**item) for item in ld]
        except FileNotFoundError:
            return []


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
