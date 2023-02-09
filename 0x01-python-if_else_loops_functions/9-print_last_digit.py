#!/usr/bin/python3

def print_last_digit(number):
    n = abs(number)
    r = n % 10
    print("{}".format(r), end="")
    return r
