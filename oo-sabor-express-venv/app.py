"""
Comando para criação de um ambiente virtual python "venv"
1 - python -m venv venv
2 - .venv\Scripts\activate.bat  ativa a venv
3 - deactivate desativa o ambiente
4 -  pip install requests
5 - pip freeze
6 - pip freeze > requiriments.txt - cria um arquivo txt com todos os comandos para serem executados
7 - Instalando fastApi - pip install fastapi
8 - pip install uvicorn
9 - pip freeze > requirements.txt - aponta todas as novas dependências instaladas no arquivo txt requirements
"""
import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()#Json com uma lista de dicionarios contendo chave e valor.
    dados_restaurante = {}#Criando um dicionário vazio
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:#Se a chave não estiver dentro da lista de dicionários
            dados_restaurante[nome_do_restaurante] = []#Criando uma lista vazia.
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "decription": item['description']
        })

else:
    print(f'O erro foi {response.status_code}')

#Criando arquivo em python
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'#Criar arquivo json
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:#Escrevendo arquivo
        json.dump(dados, arquivo_restaurante, indent=4)#gerando arquivo passando os dados, o arquivo e a identação dos dados.