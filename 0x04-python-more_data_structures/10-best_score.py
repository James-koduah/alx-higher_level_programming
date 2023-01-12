#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    a = list(a_dictionary.keys())
    maxi = -1000
    ke = []
    for elem in a:
        ke.append(a_dictionary[elem])
    for elem in ke:
        if elem > maxi:
            maxi = elem
    for elem in a:
        if a_dictionary[elem] == maxi:
            return elem
