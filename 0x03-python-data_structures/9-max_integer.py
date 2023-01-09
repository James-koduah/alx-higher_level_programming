#!/usr/bin/python3

def max_integer(my_list=[]):
    a = -1000
    le = len(my_list)
    if le == 0:
        return None

    for x in my_list:
        if x > a:
            a = x
    return a
