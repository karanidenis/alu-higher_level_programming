#!/usr/bin/python3
"""mutliply 2 matrices using Numpy module """

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    :param m_a: matrix a
    :param m_b: matrix b
    :return: using Numpy do m_a*m_b
    """
    return np.matmul(m_a, m_b)


if __name__ == '__main__':
    square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
