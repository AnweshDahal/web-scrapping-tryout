"""
  Automated script to scrape Flipkart for products and prices.
"""

from selenium import webdriver
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd

def scrapper(site, product_name, page=1):
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--ignore-certificate-errors')
  chrome_options.add_argument('--incognito')
  # chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(f'{site}/search?q={urllib.parse.quote(product_name)}&page={page}')
  content = driver.page_source
  driver.quit()
  return content

# Site URL
site = 'https://www.flipkart.com'
product_name = 'apple'

content = scrapper(site, product_name)
# Navigating to the site


soup = BeautifulSoup(content, 'html.parser')

# Get the number of pages
pagination = soup.find_all('a', attrs={'class': 'ge-49M'})
print(len(pagination))

# Skimming through the pagination

# products = soup.find_all('div', { 'class': "_1AtVbE"})

title = list()
price = list()

for i in range(1, len(pagination) + 1):
  print("Scrapping Page {}".format(i))
  content = scrapper(site, product_name, i)
  soup = BeautifulSoup(content, 'html.parser')
  products = soup.find_all('div', { 'class': "_1AtVbE"})
  for product in products:
    print("Storing Product...")
    if product.find('div', {'class': '_4rR01T'}):
      title.append(product.find('div', {'class': '_4rR01T'}).decode_contents())
      price.append(product.find('div', { 'class': '_30jeq3 _1_WHN1'}).decode_contents())

dictionary = {'title': title, 'price': price}

df = pd.DataFrame(dictionary)
df.to_csv(f'flipkart_{product_name}.csv', index=False)

    