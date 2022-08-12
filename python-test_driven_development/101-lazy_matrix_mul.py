#!/usr/bin/python3
"""multiply 2 matrices using Numpy module """

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    :param m_a: matrix a
    :param m_b: matrix b
    :return: using Numpy do m_a*m_b
    """
    return np.matmul(m_a, m_b)
