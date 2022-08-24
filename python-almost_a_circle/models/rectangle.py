#!/usr/bin/python3
""" class Rectangle that inherits from Base"""
from .base import Base


class Rectangle(Base):
    """class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        :param width, height, x, y and id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, values):
        """ width setter"""
        if type(values) is not int:
            raise TypeError("width must be an integer")
        if values <= 0:
            raise ValueError("width must be > 0")
        self.__width = values

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, values):
        """ height setter"""
        if type(values) is not int:
            raise TypeError("height must be an integer")
        if values <= 0:
            raise ValueError("height must be > 0")
        self.__height = values

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, values):
        """ x setter"""
        if type(values) is not int:
            raise TypeError("x must be an integer")
        if values <= 0:
            raise ValueError("x must be >= 0")
        self.__x = values

    @property
    def y(self):
        """ y getter"""
        return self.__y

    @y.setter
    def y(self, values):
        """y setter"""
        if type(values) is not int:
            raise TypeError("y must be an integer")
        if values <= 0:
            raise ValueError('y must be >= 0')
        self.__y = values

    def area(self):
        """ returns the area of the rectangle object """
        return self.width * self.height

    def display(self):
        """ displays a rectangle """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ str special method """
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returns a dictionary with properties """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
