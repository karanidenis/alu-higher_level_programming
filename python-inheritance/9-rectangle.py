#!/usr/bin/python3
"""
class Rectangle inherits from class BaseGeometry
after importing the module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle that inherits from class BaseGeometry"""
    def __init__(self, width, height):
        """
        initialises rectangle
        :param width:
        :param height:
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        :returns area of rectangle:
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """ string representation """
        print("[{}] {}/{}".format(type(self).__name__,
                                  self.__width, self.__height))


if __name__ == '__main__':
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
