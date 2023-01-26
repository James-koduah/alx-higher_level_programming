#!/usr/bin/python3
import random
number = random.randint(-10, 10)
h = ""
if number > 0:
    h = "is positive"
elif number == 0:
    h = "is zero"
else:
    h = "is negative"

print("{} {}".format(number, h))
