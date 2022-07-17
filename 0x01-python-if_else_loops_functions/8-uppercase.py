#!/usr/bin/python3
def uppercase(str):
    s = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            s += "{:c}".format(ord(c) - 32)
        else:
            s += c
    print("{:s}".format(s))
