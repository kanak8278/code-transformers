# test_factorial.py
import unittest
from factorial.new_helper import factorial, factorial_cache

class TestFactorial(unittest.TestCase):
    
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_two(self):
        self.assertEqual(factorial(2), 2)
    
    def test_factorial_five(self):
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_ten(self):
        self.assertEqual(factorial(10), 3628800)
    
    def test_factorial_cache(self):
        # Clear cache and test caching behavior
        factorial_cache.clear()
        self.assertEqual(factorial(5), 120)
        self.assertIn(5, factorial_cache)
        self.assertEqual(factorial_cache[5], 120)
    
    def test_factorial_large_number(self):
        self.assertEqual(factorial(20), 2432902008176640000)

if __name__ == '__main__':
    unittest.main()
