#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n, return_list=[]):
    """finds the pascal's value for the n number"""
    def factorial(integer):
        if integer <= 1:
            return 1
        elif integer <= 1:
            return integer
        return integer * factorial(integer - 1)

    if n < 0:
        return []
    if n >= 0:
        pascal_triangle(n - 1, return_list)
        row = [
            factorial(n) // (factorial(n - base) * factorial(base))
            for base in range(n + 1)
            ]
        return_list.append(row)
    return return_list
