#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print("{:s}".format(' '.join(map(str, row))))