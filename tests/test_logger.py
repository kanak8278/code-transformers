import unittest
from io import StringIO
import sys

from result import log

# def log(message, level="INFO"):
#     color_codes = {
#         "INFO": "\033[94m",
#         "WARNING": "\033[93m",
#         "ERROR": "\033[91m",
#     }
#     if level not in color_codes:
#         raise ValueError(f"Unsupported log level: {level}")
#     print(f"[{level}], Message:{message}, color:{color_codes[level]}")

class TestLogFunction(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset redirect.
        sys.stdout = sys.__stdout__

    def test_log_info(self):
        log("This is an info message")
        self.assertEqual(self.held_output.getvalue().strip(), "[INFO], Message:This is an info message, color:\033[94m")

    def test_log_warning(self):
        log("This is a warning message", "WARNING")
        self.assertEqual(self.held_output.getvalue().strip(), "[WARNING], Message:This is a warning message, color:\033[93m")

    def test_log_error(self):
        log("This is an error message", "ERROR")
        self.assertEqual(self.held_output.getvalue().strip(), "[ERROR], Message:This is an error message, color:\033[91m")

    def test_log_invalid_level(self):
        with self.assertRaises(ValueError) as context:
            log("This is an invalid level message", "DEBUG")
        self.assertTrue("Unsupported log level: DEBUG" in str(context.exception))

    def test_log_empty_message(self):
        log("")
        self.assertEqual(self.held_output.getvalue().strip(), "[INFO], Message:, color:\033[94m")

    def test_log_custom_info(self):
        log("Custom info message", "INFO")
        self.assertEqual(self.held_output.getvalue().strip(), "[INFO], Message:Custom info message, color:\033[94m")

    def test_log_custom_warning(self):
        log("Custom warning message", "WARNING")
        self.assertEqual(self.held_output.getvalue().strip(), "[WARNING], Message:Custom warning message, color:\033[93m")

    def test_log_custom_error(self):
        log("Custom error message", "ERROR")
        self.assertEqual(self.held_output.getvalue().strip(), "[ERROR], Message:Custom error message, color:\033[91m")

if __name__ == "__main__":
    unittest.main()
