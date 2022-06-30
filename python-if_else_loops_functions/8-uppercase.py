#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) <= 123 and ord(i) >= 97:
             print("{}.upper".format(str))
