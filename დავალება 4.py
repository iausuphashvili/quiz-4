import csv
import time

import requests
from bs4 import BeautifulSoup

rows = []

for i in range(1, 6):
    content = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    bs = BeautifulSoup(content.text, 'html.parser')
    quote_blocks = bs.find_all('div', class_='quote')
    for quote_block in quote_blocks:
        page = f"Page: {i}"
        quote = quote_block.find('span', class_='text').text
        author = quote_block.find('small', class_='author').text
        tags = ' '.join([i.text for i in quote_block.find_all('a', class_='tag')])
        rows.append([page, quote, author, tags])
    time.sleep(15)

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
