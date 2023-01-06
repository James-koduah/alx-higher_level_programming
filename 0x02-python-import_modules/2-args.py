#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    n = len(sys.argv)

    for x in range(1, n):
        print("{}: {}".format(x, sys.argv[x]))
