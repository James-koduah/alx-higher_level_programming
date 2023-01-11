#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    c = 0
    n = len(my_list)
    for i in range(0, n):
        z = my_list[i]
        b = my_list.index(z)
        if a == b:
            c = c + z
        a = a + 1
    return c
