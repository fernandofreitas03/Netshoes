import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.netshoes.com.br/chuteiras'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')
chuteiras = soup. find_all(
    'div', class_='item-card card-desktop card-with-rating lazy-price item-desktop--3')
ultima_pagina = soup.find('a', class_="last")

chuteira = chuteiras[0]
titulo = chuteira.find(
    'div', class_="item-card__description__product-name").get_text()
preco = chuteira.find('span', class_="full-mounted-price").get_text()

images = soup.find_all('img')

for img in images:
    img_url = img['src']
    if 'https://' not in img_url:
        img_url = 'https:' + img_url
    urllib.request.urlretrieve(img_url)

print()
