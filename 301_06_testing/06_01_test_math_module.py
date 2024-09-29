# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.



import unittest
import math

class TestMathModule(unittest.TestCase):
    
    def test_sqrt(self):
        """Test the sqrt function for correct results."""
        self.assertEqual(math.sqrt(4), 2)  # 4^0.5 = 2
        self.assertEqual(math.sqrt(16), 4)  # 16^0.5 = 4
        self.assertAlmostEqual(math.sqrt(2), 1.4142135, places=5)  # sqrt(2) ≈ 1.4142135
        with self.assertRaises(ValueError):
            math.sqrt(-1)  # sqrt of a negative number should raise a ValueError

    def test_factorial(self):
        """Test the factorial function for correct results."""
        self.assertEqual(math.factorial(5), 120)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
        self.assertEqual(math.factorial(0), 1)  # 0! is defined as 1
        self.assertEqual(math.factorial(1), 1)  # 1! = 1
        with self.assertRaises(ValueError):
            math.factorial(-1)  # Factorial of negative number should raise a ValueError

if __name__ == "__main__":
    unittest.main()