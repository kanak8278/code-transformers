1. Places which use external variable are difficult to handle.
factorial_cache = {}
```python
def factorial(n):
    if n in factorial_cache:
        return factorial_cache[n]
    if n == 0:
        return 1
    result = n * factorial(n - 1)
    factorial_cache[n] = result
    return result
```