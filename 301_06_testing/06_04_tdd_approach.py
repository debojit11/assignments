# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.


import unittest

class TestSimpleFunctions(unittest.TestCase):
    
    # Test cases for add_numbers function
    def test_add_numbers_positive(self):
        """Test add_numbers with positive integers."""
        result = add_numbers(3, 5)  # Expected 3 + 5 = 8
        self.assertEqual(result, 8)

    def test_add_numbers_negative(self):
        """Test add_numbers with negative integers."""
        result = add_numbers(-3, -5)  # Expected -3 + (-5) = -8
        self.assertEqual(result, -8)

    def test_add_numbers_mixed(self):
        """Test add_numbers with a positive and a negative integer."""
        result = add_numbers(3, -5)  # Expected 3 + (-5) = -2
        self.assertEqual(result, -2)

    def test_add_numbers_type_error(self):
        """Test add_numbers with non-numeric input."""
        with self.assertRaises(TypeError):
            add_numbers("3", 5)  # Should raise TypeError for invalid input type

    # Test cases for read_file function
    def test_read_file_success(self):
        """Test read_file with a valid file path."""
        content = read_file("test_file.txt")  # Assuming the file exists with content
        self.assertEqual(content, "This is a test file.")  # The file contains this text

    def test_read_file_file_not_found(self):
        """Test read_file with a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            read_file("non_existent_file.txt")  # Should raise FileNotFoundError

    def test_read_file_empty(self):
        """Test read_file with an empty file."""
        content = read_file("empty_file.txt")  # Assuming this file exists but is empty
        self.assertEqual(content, "")  # The file has no content

if __name__ == "__main__":
    unittest.main()