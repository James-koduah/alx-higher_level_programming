#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total = 0
    n = len(sys.argv)

    for x in range(1, n):
        total += int(sys.argv[x])

    print("{}".format(total))
