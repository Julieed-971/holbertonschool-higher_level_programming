#!/usr/bin/python3
def uppercase(str):
    temp = ""
    for c in str:
        if ord(c) in range(97, 123):
            temp += chr(ord(c) - 32)
        else:
            temp += c
    print("{}".format(temp))
