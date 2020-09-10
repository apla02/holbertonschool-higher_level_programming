#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matriz = [[j ** 2 for j in i] for i in matrix]
    return new_matriz
