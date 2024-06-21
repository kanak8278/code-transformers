# test_sum_of_squares.py
import unittest
from examples.sum_of_squares.new_helper import sum_of_squares

class TestSumOfSquaresFormula(unittest.TestCase):

    def test_positive_integer_five(self):
        self.assertEqual(sum_of_squares(5), 55)

    def test_positive_integer_one(self):
        self.assertEqual(sum_of_squares(1), 1)

    def test_positive_integer_ten(self):
        self.assertEqual(sum_of_squares(10), 385)

    def test_large_number(self):
        self.assertEqual(sum_of_squares(100), 338350)

    def test_invalid_input_zero(self):
        with self.assertRaises(ValueError):
            sum_of_squares(0)

    def test_invalid_input_negative(self):
        with self.assertRaises(ValueError):
            sum_of_squares(-5)

    def test_edge_case(self):
        self.assertEqual(sum_of_squares(1), 1)

class CountingTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success_count = 0

    def addSuccess(self, test):
        super().addSuccess(test)
        self.success_count += 1

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSumOfSquaresFormula)
    runner = unittest.TextTestRunner(resultclass=CountingTestResult)
    result = runner.run(suite)
    return result

if __name__ == '__main__':
    result = run_tests()
    print(f"Number of test cases passed: {result.success_count}")
