#!/usr/bin/python3
'''Divides a matrix of integers'''


def matrix_divided(matrix, div):
    '''
    Divide a matrix of integers

    Parameters
    ----------
    matrix: list
        list of a list of integers
    div: int
        integer to divide the matrix with

    Raises
    ------
    TypeError
        If matrix is not of type list
        If matrix element are different size
        If element of matrix are not int or float
        If div is not a number
    ZeroDivisionError
        If div is zero
    Returns
    -------
    new_matrix
        A new matrix containing the result of the division of the list
    '''
    if all(type(matrix_ele) is not list or len(matrix_ele) <= 0
            for matrix_ele in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(matrix_ele) is len(matrix[0]) for matrix_ele in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not all(isinstance(element, (int, float))
               for matrix_ele in matrix for element in matrix_ele):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round((x / div), 2) for x in row] for row in matrix]
    return new_matrix
