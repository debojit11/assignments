# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)

# test_average_calculator.py

import unittest
from average_calculator import calculate_average

class TestCalculateAverage(unittest.TestCase):

    def test_average_of_positive_numbers(self):
        """Test the average of a list of positive numbers."""
        result = calculate_average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3.0)  # Expected average: 3

    def test_average_of_mixed_numbers(self):
        """Test the average of a list with positive and negative numbers."""
        result = calculate_average([-2, 2, -3, 3])
        self.assertAlmostEqual(result, 0.0)  # Expected average: 0
    
    def test_empty_list(self):
        """Test that the function raises a ValueError for an empty list."""
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_failing_case(self):
        """This test is designed to fail."""
        result = calculate_average([1, 1, 1, 1])
        self.assertEqual(result, 2)  # Incorrect expected value (it will fail)

if __name__ == "__main__":
    unittest.main()
