#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    cp = my_list.copy()
    a = len(my_list)

    if idx > a-1:
        return my_list
    if idx < 0:
        return cp
    cp[idx] = element
    return cp
