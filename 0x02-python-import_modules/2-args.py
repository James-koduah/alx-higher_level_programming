#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    b = 's'
    s = ':'
    n = len(sys.argv)
    if n == 1:
        s = '.'
    if n == 2:
        b = ''


    print("{} argument{}{}".format(n-1, b, s))
    for x in range(1, n):
        print("{}: {}".format(x, sys.argv[x]))
