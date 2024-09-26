# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.


from bs4 import BeautifulSoup
import requests

def fetch_url(url):
    """Fetches the URL of the webpage to scrape."""
    response = requests.get(url)
    return response.text

def save_to_file(content, filename):
    """Saves the scraped content to a file."""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(content)

def read_from_file(filename):
    """Reads the content from a file."""
    with open(filename, 'r', encoding="utf-8") as file:
        return file.read()
def parse_books(content):
    """parse html content and get the books title and price"""
    soup = BeautifulSoup(content, 'html.parser')
    books = soup.find_all('article', class_='product-pod')

    book_list=[]
    for book in books:
        title = book.h3.a['title']
        price = book.find("p", class_="price_color").text
        book_list.append((title, price))
        return book_list

def main():
    url = "http://books.toscrape.com/"
    filename = "books_to_scrape.html"

    html_content = fetch_url(url)
    save_to_file(html_content, filename)

    content = read_from_file(filename)
    books = parse_books(content)

    for title, price in books:
        print(f"Title: {title}, Price: {price}")

if __name__=="__main__":
    main()