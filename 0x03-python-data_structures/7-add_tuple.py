#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    alen = len(tuple_a)
    blen = len(tuple_b)
    a1 = 0
    b1 = 0
    a2 = 0
    b2 = 0
    if alen == 1:
        a2 = 0
        a1 = tuple_a[0]
    elif alen == 0:
        a1 = 0
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if blen == 1:
        b2 = 0
        b1 = tuple_b[0]
    elif blen == 0:
        b1 = 0
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    fir = a1 + b1
    sec = a2 + b2

    tu = fir, sec
    return tu
