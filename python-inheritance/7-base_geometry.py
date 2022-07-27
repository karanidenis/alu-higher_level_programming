#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:
    """
    function
    """
    def area(self):
        """
        parameter self
        raise and exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        :param name:
        :param value:
        :return:
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


if __name__ == '__main__':
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
