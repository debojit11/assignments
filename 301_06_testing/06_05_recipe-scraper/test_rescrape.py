# Write a unittest test suite to test the rescrape module

# test_rescrape.py

import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
import rescrape

class TestRescrape(unittest.TestCase):

    @patch('rescrape.requests.get')
    def test_get_page_content(self, mock_get):
        """Test that get_page_content returns the response from a URL."""
        # Mock the requests.get to return a custom response
        mock_response = MagicMock()
        mock_response.text = "Fake HTML content"
        mock_get.return_value = mock_response

        # Call the function
        result = rescrape.get_page_content("https://fakeurl.com")

        # Check that the function returns the mocked response
        self.assertEqual(result.text, "Fake HTML content")
        mock_get.assert_called_once_with("https://fakeurl.com")

    def test_make_soup(self):
        """Test that make_soup correctly creates a BeautifulSoup object."""
        html = "<html><body><p>Test</p></body></html>"
        soup = rescrape.make_soup(html)

        # Check if BeautifulSoup object was created properly
        self.assertIsInstance(soup, BeautifulSoup)
        self.assertEqual(soup.p.text, "Test")

    @patch('rescrape.get_page_content')
    def test_get_html_content(self, mock_get_page_content):
        """Test get_html_content returns HTML text from a URL."""
        mock_get_page_content.return_value.text = "HTML Content"
        
        # Call the function
        result = rescrape.get_html_content("https://fakeurl.com")
        
        # Check that the function returns the expected HTML content
        self.assertEqual(result, "HTML Content")
        mock_get_page_content.assert_called_once_with("https://fakeurl.com")

    def test_get_recipe_links(self):
        """Test get_recipe_links extracts URLs from a BeautifulSoup object."""
        html = '<html><body><a href="recipe1.html"></a><a href="recipe2.html"></a></body></html>'
        soup = BeautifulSoup(html, "html.parser")

        # Call the function
        result = rescrape.get_recipe_links(soup)

        # Verify that it returns the correct links
        self.assertEqual(result, ["recipe1.html", "recipe2.html"])

    def test_get_author(self):
        """Test get_author extracts the author name from a BeautifulSoup object."""
        html = '<html><body><p class="author">by John Doe</p></body></html>'
        soup = BeautifulSoup(html, "html.parser")

        # Call the function
        result = rescrape.get_author(soup)

        # Verify that the author is correctly extracted
        self.assertEqual(result, "John Doe")

    def test_get_recipe(self):
        """Test get_recipe extracts the recipe text from a BeautifulSoup object."""
        html = '<html><body><div class="md">This is the recipe content.</div></body></html>'
        soup = BeautifulSoup(html, "html.parser")

        # Call the function
        result = rescrape.get_recipe(soup)

        # Verify that the recipe text is correctly extracted
        self.assertEqual(result, "This is the recipe content.")

if __name__ == "__main__":
    unittest.main()