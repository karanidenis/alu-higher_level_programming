#!/usr/bin/python3
""" class Myth inherits from int"""


class MyInt(int):
    """ class as a rebel"""

    def __eq__(self, value):
        """Not equating the operator"""
        return self.real != value

    def __ne__(self, value):
        """Equating the operator"""
        return self.real == value


if __name__ == '__main__':
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
