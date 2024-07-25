#!usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of integers representing the Pascal's triangle of n"""
    result = []

    if n > 0:
        for i in range(1, n + 1):
            level = []
            x = 1
            for j in range(1, i + 1):
                level.append(x)
                x = x * (i - j) // j
            result .append(level)

    return result
