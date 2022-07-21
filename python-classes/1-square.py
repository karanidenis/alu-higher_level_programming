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
        self.size = None
        if not isinstance(size, int):
            raise TypeError

        if size < 0:
            raise ValueError

        self.__size = size
