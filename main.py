import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Scrapping
url = requests.get('https://pokemondb.net/pokedex/all')
soup = BeautifulSoup(url.text, 'html.parser')

# Filtro para achar as informações na página
lista_pokemon_nome = soup.find_all('a', class_='ent-name')
lista_pokemon_tipos = soup.find_all('td', class_='cell-icon')
lista_pokemon_status = soup.find_all('td', class_='cell-num')

print(lista_pokemon_nome)