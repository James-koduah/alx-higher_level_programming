#!/usr/bin/python3

def no_c(my_string):
    str = ''
    a = len(my_string)
    for x in range(0, a):
        if my_string[x] != 'c' and my_string[x] != 'C':
            str += my_string[x]

    return (str)
