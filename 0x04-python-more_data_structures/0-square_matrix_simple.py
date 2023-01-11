#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    final = []
    for i in matrix:
        new_matrix = list(map((lambda x: x ** 2), i))
        final.append(new_matrix)
    return final
