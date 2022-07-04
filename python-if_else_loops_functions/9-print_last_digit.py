#!/usr/bin/python3
def print_last_digit(number):
    last_digit = int(str(number)[-1])
    if number < 0:
        last_digit = -last_digit
    print("{}".format(last_digit), end=''
    return last_digit
