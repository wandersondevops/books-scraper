import requests
from bs4 import BeautifulSoup
import time

BASE_URL = 'http://books.toscrape.com/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

def fetch_page(url):
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            return response.text
        except (requests.RequestException, requests.Timeout) as e:
            print(f"Error fetching {url}: {e}")
            if attempt < MAX_RETRIES - 1:
                print(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"Failed to fetch {url} after {MAX_RETRIES} attempts")
                raise

def parse_books(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    books = []
    for book in soup.select('article.product_pod'):
        title = book.select_one('h3 a').attrs['title']
        price = book.select_one('p.price_color').text
        availability = book.select_one('p.availability').text.strip()
        books.append({
            'title': title,
            'price': price,
            'availability': availability
        })
    return books

def save_books(books):
    url = "http://web:8000/books/"
    headers = {"Content-Type": "application/json"}
    for book in books:
        response = requests.post(url, json=book, headers=headers)
        if response.status_code == 200:
            print(f"Saved book: {book['title']}")
        else:
            print(f"Failed to save book: {book['title']}, status code: {response.status_code}")

if __name__ == "__main__":
    # Wait for the API to be ready
    time.sleep(10)
    page_content = fetch_page(BASE_URL)
    books = parse_books(page_content)
    save_books(books)
