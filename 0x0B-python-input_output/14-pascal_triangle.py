#!/usr/bin/python3
'''
    class of Student
'''


def pascal_triangle(n):
    '''
    function to make a triangle of pascal
    '''
    pascal = []
    if n <= 0:
        return pascal
    if n == 1:
        pascal.extend([1])
        return pascal
    if n > 1:
        pascal = [[1], [1, 1]]
        for i in range(1, n - 1):
            linea = [1]
            for j in range(0, len(pascal[i]) - 1):
                linea.extend([pascal[i][j] + pascal[i][j+1]])
            linea += [1]
            pascal.append(linea)
        return pascal
