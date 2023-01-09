#!/usr/bin/python3

def print_list_integer(my_list=[]):
    a = len(my_list)
    for x in range(0, a):
        print("{:d}".format(my_list[x]))
