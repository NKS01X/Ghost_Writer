import unittest
from sub import sub

class TestSubFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sub(5, 3), 2)
    
    def test_negative_numbers(self):
        self.assertEqual(sub(-2, -3), 1)
    
    def test_zero_difference(self):
        self.assertEqual(sub(10, 10), 0)
    
    def test_positive_negative(self):
        self.assertEqual(sub(5, -3), 8)
    
    def test_negative_positive(self):
        self.assertEqual(sub(-5, 3), -8)

if __name__ == '__main__':
    unittest.main()