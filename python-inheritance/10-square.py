#!/usr/bin/python3
""" class Square inherits from module 9-rectangle.py"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square"""

    def __init__(self, size):
        """ initialises square """

        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size


if __name__ == '__main__':
    s = Square(13)

    print(s)
    print(s.area())
