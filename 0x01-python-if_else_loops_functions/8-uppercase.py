#!/usr/bin/python3

def uppercase(str):
    a = ''
    for i in str:
        b = ord(i)
        if b >= 97 and b <= 122:
            b = b - 32
        a += chr(b)
    print("{}".format(a))
