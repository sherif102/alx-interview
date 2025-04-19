"""
Pascal's triangle
"""


def pascal_triangle(n, return_list=[]):
    """finds the pascal's value for the n number"""
    def factorial(integer):
        if integer <= 1:
            return integer
        return integer * factorial(integer - 1)

    if n <= 0:
        return []
    elif n > 0:
        pascal_triangle(n - 1, return_list)
        result = [
            factorial(n) // (factorial(n - base) * factorial(base))
            for base in range(1, n)
            ]
        result.append(1)
        if len(result) > 0:
            result.insert(0, 1)
        if n == 1:
            return_list.append([1])
        return_list.append(result)
    return return_list
