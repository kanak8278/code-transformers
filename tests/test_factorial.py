# test_factorial.py
import unittest
from examples.factorial.new_helper import factorial, factorial_cache

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

class CountingTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success_count = 0

    def addSuccess(self, test):
        super().addSuccess(test)
        self.success_count += 1

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFactorial)
    runner = unittest.TextTestRunner(resultclass=CountingTestResult)
    result = runner.run(suite)
    return result

if __name__ == '__main__':
    result = run_tests()
    print(f"Number of test cases passed: {result.success_count}")
