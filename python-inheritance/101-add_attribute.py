#!/usr/bin/python3
"""function that adds a new attribute if possible"""


def add_attribute(obj, attr, value):
    """
    :param obj: add object
    :param attr: name of attribute
    :param value: value of the attribute
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)


if __name__ == '__main__':
    class MyClass():
        pass


    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
