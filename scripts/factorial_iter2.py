def factorial_iter2(n):
    """
    Iterative: Returns n!
    """
    if n <= 1:
        return 1

    result = 1
    while n >= 1:
        result *= n
        n -= 1

    return result
