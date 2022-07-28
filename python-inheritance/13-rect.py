#!/usr/bin/python3
"""
    Module containing the `Rectangle` class that inherits the `BaseGeometry`
    class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from the `BaseGeometry` class.
    """

    def __init__(self, width, height):
        """Initializes the Rectangle instance.
        Args:
            width (int): `width` of the `Rectangle` instance.
            height (int): `height` of the `Rectangle` instance.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the `Rectangle` instance.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        string representation.
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


if __name__ == '__main__':
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
