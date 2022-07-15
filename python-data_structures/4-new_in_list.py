#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if my_list < 0 or my_list > range(len(my_list) - 1):
        return my_list.copy()
    else:
        my_list[idx] = element
        return copy
