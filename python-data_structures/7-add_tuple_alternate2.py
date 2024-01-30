#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    
    add = []
    for i in range(2):
        add.append(tuple_a[i] + tuple_b[i])
    return tuple(add)
