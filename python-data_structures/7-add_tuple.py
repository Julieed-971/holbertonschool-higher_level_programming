#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 and len(tuple_a) > 0:
        tuple_c = tuple_a[0], 0
        add = tuple(map(lambda x, y: x + y, tuple_c, tuple_b))
    elif len(tuple_b) < 2 and len(tuple_b) > 0:
        tuple_c = tuple_b[0], 0
        add = tuple(map(lambda x, y: x + y, tuple_a, tuple_c))
    elif len(tuple_b) < 1:
        tuple_c = 0, 0
        add = tuple(map(lambda x, y: x + y, tuple_a, tuple_c))
    elif len(tuple_a) < 1:
        tuple_c = 0, 0
        add = tuple(map(lambda x, y: x + y, tuple_a, tuple_c))
    else:
        add = tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    return add
