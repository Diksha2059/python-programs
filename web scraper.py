import requests
from bs4 import BeautifulSoup

URL = "http://quotes.toscrape.com"
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

    print(f"\nQuote: {text}")
    print(f"Author: {author}")
    print(f"Tags: {', '.join(tags)}")
