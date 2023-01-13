#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    mul = 0
    ad = 0
    for elem in my_list:
        mul += elem[0] * elem[1]
        ad += elem[1]
    return mul / ad
