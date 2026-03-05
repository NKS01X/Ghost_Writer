import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_zero(self):
        result = add(10, 0)
        self.assertEqual(result, 10)

    def test_add_positive_negative(self):
        result = add(7, -4)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        result = add(2.5, 3.5)
        self.assertAlmostEqual(result, 6.0)

if __name__ == '__main__':
    unittest.main()