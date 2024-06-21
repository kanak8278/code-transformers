def sum_of_squares(n):
    """
    Calculate the sum of the squares of the first n natural numbers.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    return sum(i ** 2 for i in range(1, n + 1))
