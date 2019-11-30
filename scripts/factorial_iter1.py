def factorial_iter1(n):
    """
    Iterative: Returns n!
    """
    if n <= 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result
