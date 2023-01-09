#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for a in x:
            print("{:d} ".format(a), end='')
        print("")
