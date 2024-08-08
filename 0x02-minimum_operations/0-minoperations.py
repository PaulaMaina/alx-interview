#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """Calculates the fewest number of operations to result in H characters"""
    if n < 2:
        return 0
    operations = 0
    root = 2
    while root <= n:
        if n % root == 0:
            operations += root
            n = n / root
            root -= 1
        root += 1

    return operations
