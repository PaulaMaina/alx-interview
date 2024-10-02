#!/usr/bin/python3
"""Prime Game Module."""


def isWinner(x, nums):
    """Determines the winner of a prime game session over `x` rounds."""
    if x < 1 or not nums:
        return None

    maria_score, ben_score = 0, 0

    # Find the maximum number in nums and generate primes up to that number
    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    is_prime[0] = False
    is_prime[1] = False  # 1 is not a prime number

    for i in range(2, max_num + 1):
        if is_prime[i]:
            for j in range(i * 2, max_num + 1, i):
                is_prime[j] = False

    # Loop through each round and count prime numbers up to each value in nums
    for round_num in range(x):
        current_num = nums[round_num]
        prime_count = sum(is_prime[:current_num + 1])

        if prime_count % 2 == 1:
            maria_score += 1  # Maria wins if the count is odd
        else:
            ben_score += 1  # Ben wins if the count is even

    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    else:
        return None
