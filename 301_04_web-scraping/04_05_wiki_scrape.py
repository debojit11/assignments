# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.


import requests
from bs4 import BeautifulSoup
import re

# URL of the Wikipedia page on Web Scraping
URL = "https://en.wikipedia.org/wiki/Web_scraping"

# Function to fetch and parse the Wikipedia page
def fetch_wikipedia_page(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return BeautifulSoup(response.text, 'html.parser')

# Function to extract and filter links
def extract_links(soup):
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Only include links that lead to another Wikipedia article
        if href.startswith('/wiki/') and not href.startswith('/wiki/Special:'):
            links.append('https://en.wikipedia.org' + href)
    return links

# Function to save text content to a file
def save_text_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

# Function to find all numbers in the text
def find_numbers_in_text(text):
    return re.findall(r'\d+', text)

# Main code
if __name__ == "__main__":
    # Fetch the Web Scraping Wikipedia page
    soup = fetch_wikipedia_page(URL)
    
    # Extract links from the page
    links = extract_links(soup)
    
    # Print the first few links (optional)
    print("Extracted links:")
    for link in links[:5]:  # Display the first 5 links
        print(link)

    # Follow the first link to another Wikipedia article
    if links:
        next_article_url = links[0]  # Choose the first link to follow
        print(f"\nFollowing link: {next_article_url}")

        next_soup = fetch_wikipedia_page(next_article_url)
        
        # Extract text content from the new article
        article_text = next_soup.get_text()
        
        # Save the text content to a local file
        save_text_to_file(article_text, 'wiki_article.txt')
        print("Article text saved to 'wiki_article.txt'.")

        # Find all numbers in the text
        numbers = find_numbers_in_text(article_text)
        print(f"Found numbers: {numbers}")
    else:
        print("No valid links found.")
