#!/usr/bin/python3
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def nqueens(n, i=0, a=[], b=[], c=[]):
    """Finds the possible positions"""
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from nqueens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """Solves the problem"""
    i = []
    j = 0
    for sol in nqueens(n, 0):
        for x in sol:
            i.append([j, x])
            j += 1
        print(i)
        i = []
        j = 0


solve(n)
