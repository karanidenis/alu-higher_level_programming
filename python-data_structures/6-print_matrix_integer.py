#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in matrix:
            x = []
            y = []
            for j in col:
                y.append(j)
            for i in row:
                x.append(i)
            print("{:d}".format(matrix[i][j]), end = "")
