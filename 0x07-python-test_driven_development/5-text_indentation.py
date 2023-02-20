#!/usr/bin/python3

'''text_indentation'''


def text_indentation(text):
    '''does something'''
    b = False

    if type(text) != str:
        raise TypeError("text must be a string")

    for x in range(0, len(text)):
        if b is True and text[x] != ' ':
            b = False
        if b is True and text[x] == ' ':
            continue

        print(text[x], end="")
        if text[x] == '.' or text[x] == '?' or text[x] == ':':
            print('\n')
            b = True
