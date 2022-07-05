#!/usr/bin/python3

def add(a, b):
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a + b)))


def main(a, b):
    a = 10
    b = 5
    print("{} - {} = {}".format(a, b, sub(a-b)))


def main(a, b):
    a = 10
    b = 5
    print("{} * {} = {}".format(a, b, mul(a*b)))


def main(a, b):
    a = 10
    b = 5
    print("{} / {} = {}".format(a, b, div(a/b)))


if __name__ == '__main__':
    main()
