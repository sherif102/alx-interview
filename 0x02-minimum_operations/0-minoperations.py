#!/usr/bin/python3
"""minimum operations"""


def minOperations(n):
    """calculates the minimum operations"""
    if n <= 1:
        return 0

    op_counter = 2
    current = 2
    copied = 1

    while current < n:
        if n % current == 0 and (n // current) % 2 == 0:
            op_counter += 2
            copied = current
            current += copied
        elif n % current == 0:
            op_counter += 2
            copied = current
            current += copied
        else:
            op_counter += 1
            current += copied

    if current > n:
        return 0

    return op_counter
