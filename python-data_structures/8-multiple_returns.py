#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if length < 1:
        start = 'None'
    else:
        start = sentence[0]
    tuple = length, start
    return tuple
