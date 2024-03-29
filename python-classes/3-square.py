#!/usr/bin/python3
"""
define a square by:
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be int, raise TypeError exception(message size must be an integer)
if size is < 0, raise ValueError exception(message size must be >= 0)
Public instance method: def area(self): returns the current square area
You are not allowed to import any module
"""


class Square:
    """ define a square"""
    def __init__(self, size=0):
        """
                Creates an instance of Square
                Args:
                    size: size of the square
                """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size**2
