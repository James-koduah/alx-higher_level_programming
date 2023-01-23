#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    hh = 0
    for x in range(x):
        try:
            print("{}".format(my_list[x]), end= "")
            hh += 1
        except IndexError:
            break
    print("")
    return hh
