#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = list(a_dictionary.keys())
    c = 0
    b = {}
    for elem in a:
        c = a_dictionary[elem]
        c = c * 2
        b[elem] = c
    return b
