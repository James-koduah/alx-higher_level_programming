#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    hh = 0
    try:
        for x in range(0, x):
            print("{}".format(my_list[x]), end= " ")
            hh += 1
    except IndexError:
            print("", end="")
    finally:
        print("")
    return hh
