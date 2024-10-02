#!/usr/bin/python3
"""Making change module"""


def makeChange(coins, total):
    """Determines the fewest number of coins neede to meet a given amount"""
    if total <= 0:
        return 0
    if not coins or coins is None:
        return -1

    change = 0
    coins = sorted(coins)[::-1]

    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change

    return -1
