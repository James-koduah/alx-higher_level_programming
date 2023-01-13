#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    ke = list(a_dictionary.keys())
    for elem in ke:
        b = a_dictionary[elem]
        if b == value:
            a_dictionary.pop(elem)
    return a_dictionary
