#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4
    content = dir(hidden_4)
    n = len(content)

    for x in range(0, n):
        if content[x][0] != "_":
            print("{}".format(content[x]))
