#!/usr/bin/python3
"""Return a matrix of integers representing the Pascal's triangle of n."""


def pascal_triangle(n):
    """Return a matrix of integers representing the Pascal's triangle of n."""

    # Return an empty list if n inferior or equal to zero
    if n <= 0:
        return []
    elif n > 0:
        # Initialize matrix to 1
        p_matrix = [[1]]
        # While number of elements of matrix inferior to n
        for i in range(n - 1):
            # Initialize list to 1
            p_list = [1]
            if i > 0:
                # While number of elements of list inferior to matrix index
                for j in range(len(p_matrix[i]) - 1):
                    # Create new list & append element from p_list
                    p_list.append(p_matrix[i][j] + p_matrix[i][j + 1])
            # Append element to the list from element at index 0
            p_list.append(p_matrix[i][0])
            # Append list to the matrix
            p_matrix.append(p_list)
        # Return matrix
        return p_matrix
