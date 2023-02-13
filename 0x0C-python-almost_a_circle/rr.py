#!/usr/bin/python3


def hh(hh, *args):
    print(hh)
    a = args[0]
    b = args[1]
    c = args[2]
    d = args[3]
    try:
        e = args[4]
    except:
        e = 10
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

def bb(gg, **kwargs):
    if "James" in kwargs:
        print("James is present")
    else:
        print("James is not present")


def main():
    #hh(1,2,3,4,5)
    bb(8, hh="kkd", James="Kodyah")


main()
