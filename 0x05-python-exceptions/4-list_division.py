#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    final = []
    for x in range(0, list_length):
        try:
            j = my_list_1[x] / my_list_2[x]
        except TypeError:
            j = 0
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            j = 0
        except IndexError:
            print("out of range")
            j = 0
        finally:
            final.append(j)
    return (final)
