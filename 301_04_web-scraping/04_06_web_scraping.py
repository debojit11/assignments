# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

from bs4 import BeautifulSoup
import requests

# Define the URL and filename
url = "http://books.toscrape.com/"
filename = "books_to_scrape.html"

# Fetch data from the URL and save to a file
response = requests.get(url)
with open(filename, "w", encoding="utf-8") as file:
    file.write(response.text)

# Read the content from the saved file
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, features="html.parser")

# Find all book entries
books = soup.find_all("article", class_="product_pod")

# Loop through each book and print title and price
for book in books:
    title = book.h3.a['title']
    price = book.find("p", class_="price_color").text
    print(f"Title: {title}  Price: {price}")