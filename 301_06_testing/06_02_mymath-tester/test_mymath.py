# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.


import unittest
from mymath import subtract_divide, CustomZeroDivsionError

class TestSubtractDivide(unittest.TestCase):

    # Test for correct results with valid input
    def test_subtract_divide_valid(self):
        # Test case: (dividend=10, x=5, y=2) -> 10 / (5 - 2) = 10 / 3
        self.assertAlmostEqual(subtract_divide(10, 5, 2), 10 / 3)

        # Test case: (dividend=20, x=8, y=3) -> 20 / (8 - 3) = 20 / 5
        self.assertEqual(subtract_divide(20, 8, 3), 4.0)

    # Test for raising CustomZeroDivisionError when x - y == 0
    def test_subtract_divide_zero_division(self):
        # Test case: (dividend=10, x=5, y=5) -> 5 - 5 = 0 -> should raise CustomZeroDivisionError
        with self.assertRaises(CustomZeroDivsionError) as context:
            subtract_divide(10, 5, 5)

        # Ensure the error message is correct
        self.assertEqual(str(context.exception), "This won't work because 5 - 5 = 0.")

if __name__ == '__main__':
    unittest.main()
