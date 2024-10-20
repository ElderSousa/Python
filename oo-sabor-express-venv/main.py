from fastapi import FastAPI, Query
import requests
#pip install "fastapi[standard]" - instalando fastapi
#fastapi dev main.py - comando para subir o servidor
app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'Hello':'World'}

@app.get('/api/restaurante/')
def get_restaurantes(restaurante : str = Query(None)):#Quando não houver dados o valor padrão será none

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if response.status_code == 200:
        dados_json = response.json()#Json com uma lista de dicionarios contendo chave e valor.

        if restaurante is None:
            return {'Dados' : dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return  {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return('Erro' f'{response.status_code} - {response.status_code}')
