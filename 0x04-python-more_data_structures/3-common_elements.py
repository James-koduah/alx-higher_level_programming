#!/usr/bin/python3

def common_elements(set_1, set_2):
    def chec_uniq(li_1, li_2):
        c = True
        d = set()
        for elem in li_1:
            c = elem in li_2
            if c is True:
                d.add(elem)
        return d

    e = chec_uniq(set_1, set_2)
    return e
