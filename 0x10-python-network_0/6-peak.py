#!/usr/bin/python3

"""Module to find the peak in a list"""


def find_peak(list_of_integers):
    length = len(list_of_integers)
    for i in range(1, length - 1):
        cur = list_of_integers[i]
        pre = list_of_integers[i - 1]
        nex = list_of_integers[i + 1]
        if pre < cur and nex < cur:
            return cur
    for i in range(1, length - 1):
        cur = list_of_integers[i]
        pre = list_of_integers[i - 1]
        nex = list_of_integers[i + 1]
        if pre == cur and nex == cur:
            return cur
