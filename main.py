import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

class Sistema:
    def __init__(self) -> None:
        pass
    
    def database():
        global Dataframe

        # Scrapping
        url = requests.get('https://pokemondb.net/pokedex/all')
        soup = BeautifulSoup(url.text, 'html.parser')

        # Filtro para achar as informações na página
        lista_pokemon_nome = soup.find_all('a', class_='ent-name')
        lista_pokemon_tipos = soup.find_all('td', class_='cell-icon')
        lista_pokemon_status = soup.find_all('td', class_='cell-num')

        # Atribuição das Variáveis
        nomes = [nome.text for nome in lista_pokemon_nome]
        tipos = [tipo.text for tipo in lista_pokemon_tipos]
        hps = np.array([int(lista_pokemon_status[i].text.strip()) for i in range(2, len(lista_pokemon_status), 8)])
        ataques = np.array([int(lista_pokemon_status[i].text.strip()) for i in range(3, len(lista_pokemon_status), 8)])
        defesas = np.array([int(lista_pokemon_status[i].text.strip()) for i in range(4, len(lista_pokemon_status), 8)])
        ataques_especiais = np.array([int(lista_pokemon_status[i].text.strip()) for i in range(5, len(lista_pokemon_status), 8)])
        defesas_especiais = np.array([int(lista_pokemon_status[i].text.strip()) for i in range(6, len(lista_pokemon_status), 8)])
        velocidades = np.array([int(lista_pokemon_status[i].text.strip()) for i in range(7, len(lista_pokemon_status), 8)])

        Dataframe = pd.DataFrame({
            'Nome': nomes,
            'Tipo': tipos,
            'HP': hps,
            'Ataque': ataques,
            'Defesa': defesas,
            'Ataque Especial': ataques_especiais,
            'Defesa Especial': defesas_especiais,
            'Velocidade': velocidades
            })
        
    def exportar_database(tipo):

        if tipo == 'excel':
            Dataframe.to_excel('database.xlsx')
        elif tipo == 'json':
            Dataframe.to_json('database.json')

Sistema.database()
Sistema.exportar_database('json')