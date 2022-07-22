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
Public instance method: def my_print(self): that prints #:
if size is equal to 0, print an empty line
You are not allowed to import any module
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be tuple of 2 positive integers,raise TypeError exception(position must be a tuple of 2 positive integers)
"""


class Square:
    """ define a square """

    def __init__(self, size=0, position=(0, 0)):
        """
        Creates an instance of Square
        Args:
            size: size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        set and get value of position
        """

        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
