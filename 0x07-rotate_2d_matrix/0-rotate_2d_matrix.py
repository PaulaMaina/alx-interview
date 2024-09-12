#!/usr/bin/python3
"""2D matrix rotation"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise"""
    n = len(matrix)
    for x in range(int(n / 2)):
        i = n - x - 1
        for y in range(x, i):
            j = (n - 1 - y)
            temp = matrix[x][y]
            matrix[x][y] = matrix[j][x]
            matrix[j][x] = matrix[i][j]
            matrix[i][j] = matrix[y][i]
            matrix[y][i] = temp
