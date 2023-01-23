#!/usr/bin/python3
def safe_print_integer(value):
    mm = True
    try:
        print("{:d}".format(value))
    except ValueError:
        mm = False
    return mm
