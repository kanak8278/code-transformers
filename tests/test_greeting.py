import unittest
from greeting.new_helper import greet

class TestGreetFunction(unittest.TestCase):

    def test_greet_valid_input(self):
        self.assertEqual(greet("John", 30, "john@example.com", "123-456-7890"),
                         "Hello, John! You are 30 years old. We have your email as john@example.com and your phone number as 123-456-7890.")

    def test_greet_missing_name(self):
        with self.assertRaises(ValueError):
            greet("", 30, "john@example.com", "123-456-7890")

    def test_greet_missing_age(self):
        with self.assertRaises(ValueError):
            greet("John", None, "john@example.com", "123-456-7890")

    def test_greet_missing_email(self):
        with self.assertRaises(ValueError):
            greet("John", 30, "", "123-456-7890")

    def test_greet_missing_phone(self):
        with self.assertRaises(ValueError):
            greet("John", 30, "john@example.com", None)

    def test_greet_all_missing(self):
        with self.assertRaises(ValueError):
            greet("", None, "", None)

    def test_greet_partial_missing(self):
        with self.assertRaises(ValueError):
            greet("John", 30, "", None)

if __name__ == '__main__':
    unittest.main()
