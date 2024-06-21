# test_greet_function.py
import unittest
from examples.greeting.new_helper import greeting

class TestGreetFunction(unittest.TestCase):

    def test_greet_valid_input(self):
        self.assertEqual(greeting("John", 30, "john@example.com", "123-456-7890"),
                         "Hello, John! You are 30 years old. We have your email as john@example.com and your phone number as 123-456-7890.")

    def test_greet_missing_name(self):
        with self.assertRaises(ValueError):
            greeting("", 30, "john@example.com", "123-456-7890")

    def test_greet_missing_age(self):
        with self.assertRaises(ValueError):
            greeting("John", None, "john@example.com", "123-456-7890")

    def test_greet_missing_email(self):
        with self.assertRaises(ValueError):
            greeting("John", 30, "", "123-456-7890")

    def test_greet_missing_phone(self):
        with self.assertRaises(ValueError):
            greeting("John", 30, "john@example.com", None)

    def test_greet_all_missing(self):
        with self.assertRaises(ValueError):
            greeting("", None, "", None)

    def test_greet_partial_missing(self):
        with self.assertRaises(ValueError):
            greeting("John", 30, "", None)

class CountingTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success_count = 0

    def addSuccess(self, test):
        super().addSuccess(test)
        self.success_count += 1

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGreetFunction)
    runner = unittest.TextTestRunner(resultclass=CountingTestResult)
    result = runner.run(suite)
    return result

if __name__ == '__main__':
    result = run_tests()
    print(f"Number of test cases passed: {result.success_count}")
