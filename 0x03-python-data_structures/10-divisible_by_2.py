#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    bo = []
    for elem in my_list:
        if elem % 2 == 0:
            bo.append(True)
        else:
            bo.append(False)

    return bo
