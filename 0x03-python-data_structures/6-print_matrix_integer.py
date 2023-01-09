#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        i = 0
        for a in x:
            print("{:d}".format(a), end='')
            if i != (len(x) - 1):
                print(" ", end="")
            i += 1
        print("")
