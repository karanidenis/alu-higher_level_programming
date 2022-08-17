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
