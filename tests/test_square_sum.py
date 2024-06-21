import unittest
from examples.square_sum.new_helper import sum_of_squares

class TestSumOfSquaresFormula(unittest.TestCase):
    
    def test_positive_integer(self):
        self.assertEqual(sum_of_squares(5), 55)
        self.assertEqual(sum_of_squares(1), 1)
        self.assertEqual(sum_of_squares(10), 385)

    def test_large_number(self):
        self.assertEqual(sum_of_squares(100), 338350)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            sum_of_squares(0)
        with self.assertRaises(ValueError):
            sum_of_squares(-5)

    def test_edge_case(self):
        self.assertEqual(sum_of_squares(1), 1)
        
if __name__ == '__main__':
    unittest.main()
