#!/usr/bin/python3

'''print square'''
def print_square(size):
    '''Prints a representation of a square'''
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for x in range(0, size):
            print("#", end="")
        print("")
