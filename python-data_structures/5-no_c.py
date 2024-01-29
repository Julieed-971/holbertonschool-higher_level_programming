#!/usr/bin/python3

def no_c(my_string):
    new_string = my_string
    new_string = ''.join([c for c in new_string if c != 'c'])
    new_string = ''.join([c for c in new_string if c != 'C'])
    return new_string
