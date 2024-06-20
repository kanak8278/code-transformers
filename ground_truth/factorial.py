
factorial_cache = {}

def factorial(n):
    if n in factorial_cache:
        return factorial_cache[n]
    if n == 0:
        return 1
    factorial_cache[n] = n * factorial(n - 1)
    return factorial_cache[n]
