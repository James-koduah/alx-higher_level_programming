#!/usr/bin/python3


a = 0
b = 1

for i in range(0, 10):
    for j in range(b, 10):
        if i == j:
            continue
        if a == 1:
            print(", ", end="")
        print("{}{}".format(i, j), end="")
        if a == 0:
            a = 1
    b += 1
print("")
