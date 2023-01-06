#!/usr/bin/python3

import sys

n = len(sys.argv)

for x in range(1, n):
    print("{}: {}".format(x, sys.argv[x]))
