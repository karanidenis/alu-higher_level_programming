#!/usr/bin/python3
""" module class with private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None):
"""


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
