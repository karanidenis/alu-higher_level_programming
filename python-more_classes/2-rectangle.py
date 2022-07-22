#!/usr/bin/python3
"""
define class rectangle by:

private instance attribute width:
width(int) otherwise raise TypeError (width must be an integer)
if width < 0: raise ValueError (width must be >= 0)
property def width(self): to retrieve
property setter def width(self, value): to set it:

private instance height:
height(int) otherwise raise TypeError (height must be an integer)
height < 0: raise ValueError (height must be >= 0)
property def height(self): to retrieve
property setter def height(self, value): to set it:

Instantiation with optional width and height:
def __init__(self, width=0, height=0):

Public instance method:
def area(self): that returns the rectangle area
Public instance method: def perimeter(self):
that returns the rectangle perimeter:
if width or height == 0, perimeter == 0

You are not allowed to import any module

"""


class Rectangle:
    """
     define a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        creating instances with args:
        width=0 and height=0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        sets and get private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        sets and get instance attribute height
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):

        rectangle_area = self.__width * self.__height
        return rectangle_area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        rectangle_perimeter = ((self.__width*2) + (self.__height*2))
        return rectangle_perimeter


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
