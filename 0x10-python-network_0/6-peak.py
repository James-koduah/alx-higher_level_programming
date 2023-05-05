#!/usr/bin/python3

"""Module to find the peak in a list"""


def find_peak(list_of_integers):
    """Find the peak in a list of integers"""
    length = len(list_of_integers)

    if length == 0:
        return None
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers)

    half = int(length / 2)
    current = list_of_integers[half]
    next = list_of_integers[half + 1]
    previous = list_of_integers[half - 1]

    if previous < current and current > next:
        return current
    elif current < previous:
        return find_peak(list_of_integers[:half])
    else:
        return find_peak(list_of_integers[half + 1:])
