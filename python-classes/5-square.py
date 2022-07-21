#!/usr/bin/python3

"""
define a square by:
Private instance attribute: size
property def size(self): to retrieve it
property setter def size(self, value): to set it:
Instantiation with optional size: def __init__(self, size=0):
size must be int, raise TypeError exception(message size must be an integer)
if size is < 0, raise ValueError exception(message size must be >= 0)
Public instance method: def area(self): returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
You are not allowed to import any module
"""


class Square:
    """ define a square """

    def __init__(self, size=0):
        """
        Creates an instance of Square
        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Sets and gets the value of private size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """
        replace area with #
        """
        for i in range(self.__size):
            print("#" * self.__size)

        if self.__size == 0:
            print()
