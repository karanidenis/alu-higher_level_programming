#!/usr/bin/python3
# defining a square by:
# Private instance attribute: size
# Instantiation with size (no type/value verification)
# You are not allowed to import any module

class Square:
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
