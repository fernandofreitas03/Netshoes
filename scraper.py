import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse
import os

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


image = soup.find('img')  
if image:
    img_url = image.get('src')
    if img_url:
        parsed_url = urlparse(img_url)
        if not parsed_url.netloc: 
            img_url = 'https:' + img_url

        try:
            filename = os.path.join('../faculdade', os.path.basename(parsed_url.path))
            urllib.request.urlretrieve(img_url, filename)
        except Exception as e:
            print(f"Erro ao recuperar a imagem: {img_url}")
            print(f"Mensagem de erro: {str(e)}")
else:
    print("Nenhuma imagem encontrada na página.")

print(preco, titulo)