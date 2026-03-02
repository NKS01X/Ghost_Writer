import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from testt import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
    
    def test_add_positive_negative(self):
        self.assertEqual(add(10, -5), 5)
    
    def test_add_zero(self):
        self.assertEqual(add(0, 7), 7)
        self.assertEqual(add(7, 0), 7)
    
    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.7), 6.2)
    
    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

if __name__ == '__main__':
    unittest.main()