#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b = list(a_dictionary.keys())
    b.sort()
    for elem in b:
        print("{}: {}".format(elem, a_dictionary[elem]))
