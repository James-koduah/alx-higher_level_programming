#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    for x in range(a, 0, -1):
        print("{:d}".format(my_list[x - 1]))
