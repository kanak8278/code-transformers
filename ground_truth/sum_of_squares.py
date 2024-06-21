def sum_of_squares(n):
    """
    Calculate the sum of the squares of the first n natural numbers using a formula.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    return n * (n + 1) * (2 * n + 1) // 6