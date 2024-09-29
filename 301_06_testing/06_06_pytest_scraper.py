# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.
import pytest
from bs4 import BeautifulSoup
import rescrape

def test_get_page_content(monkeypatch):
    """Test that get_page_content returns the response from a URL."""
    class MockResponse:
        @property
        def text(self):
            return "Fake HTML content"

    # Use monkeypatch to replace requests.get with a mock
    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr('rescrape.requests.get', mock_get)

    # Call the function
    result = rescrape.get_page_content("https://fakeurl.com")
    assert result.text == "Fake HTML content"

def test_make_soup():
    """Test that make_soup correctly creates a BeautifulSoup object."""
    html = "<html><body><p>Test</p></body></html>"
    soup = rescrape.make_soup(html)

    # Check if BeautifulSoup object was created properly
    assert isinstance(soup, BeautifulSoup)
    assert soup.p.text == "Test"

def test_get_recipe_links():
    """Test get_recipe_links extracts URLs from a BeautifulSoup object."""
    html = '<html><body><a href="recipe1.html"></a><a href="recipe2.html"></a></body></html>'
    soup = BeautifulSoup(html, "html.parser")

    # Call the function
    result = rescrape.get_recipe_links(soup)

    # Verify that it returns the correct links
    assert result == ["recipe1.html", "recipe2.html"]

def test_get_author():
    """Test get_author extracts the author name from a BeautifulSoup object."""
    html = '<html><body><p class="author">by John Doe</p></body></html>'
    soup = BeautifulSoup(html, "html.parser")

    # Call the function
    result = rescrape.get_author(soup)

    # Verify that the author is correctly extracted
    assert result == "John Doe"

def test_get_recipe():
    """Test get_recipe extracts the recipe text from a BeautifulSoup object."""
    html = '<html><body><div class="md">This is the recipe content.</div></body></html>'
    soup = BeautifulSoup(html, "html.parser")

    # Call the function
    result = rescrape.get_recipe(soup)

    # Verify that the recipe text is correctly extracted
    assert result == "This is the recipe content."
