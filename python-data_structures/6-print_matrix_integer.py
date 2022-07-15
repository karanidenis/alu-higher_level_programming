#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row = int(input("enter digit: "))
        for col in matrix:
            col = int(input("enter digit: "))
            x = []
            y = []
            for j in range(0, col):
                y.append(0)
            for i in range(0, row):
                x.append(y)
            print("{:d}".format(x))
