import unittest
from unittest.mock import patch
import sys
import io

class TestDivision(unittest.TestCase):
    def test_div_positive_numbers(self):
        result = div(10, 2)
        self.assertEqual(result, 5.0)

    def test_div_negative_numbers(self):
        result = div(-10, -2)
        self.assertEqual(result, 5.0)

    def test_div_positive_negative(self):
        result = div(10, -2)
        self.assertEqual(result, -5.0)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_div_decimal_result(self):
        result = div(1, 2)
        self.assertEqual(result, 0.5)

    def test_main_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        if __name__ == "__main__":
            print(div(1, 2))
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "0.5")

if __name__ == "__main__":
    unittest.main()