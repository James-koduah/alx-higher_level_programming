#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    vi = set()

    def onl(se, ch, re):
        a = True
        for elem in ch:
            a = elem in se
            if a is False:
                re.add(elem)

    onl(set_1, set_2, vi)
    onl(set_2, set_1, vi)
    return vi
