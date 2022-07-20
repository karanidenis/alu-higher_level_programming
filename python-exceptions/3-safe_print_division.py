#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a = a / b
    except ZeroDivisionError:
        a = None
    finally:
        print("Inside result:", "{}".format(a))
    return a


if __name__ == '__main__':
    a = 12
    b = 4
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
