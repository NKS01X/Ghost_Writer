import unittest
from sub import sub

class TestSubtraction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sub(5, 3), 2)
    
    def test_negative_numbers(self):
        self.assertEqual(sub(-2, -3), 1)
    
    def test_zero(self):
        self.assertEqual(sub(10, 0), 10)
        self.assertEqual(sub(0, 5), -5)
    
    def test_positive_negative(self):
        self.assertEqual(sub(7, -3), 10)
        self.assertEqual(sub(-5, 2), -7)
    
    def test_large_numbers(self):
        self.assertEqual(sub(1000000, 999999), 1)

if __name__ == '__main__':
    unittest.main()