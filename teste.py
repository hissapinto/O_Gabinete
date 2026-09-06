import requests
import pandas as pd
import os



ano = input('Digite o ano para baixar os dados: ')

url_votos = f'https://dadosabertos.camara.leg.br/arquivos/votacoesVotos/csv/votacoesVotos-{ano}.csv'
url_votacoes = f'https://dadosabertos.camara.leg.br/arquivos/votacoes/csv/votacoes-{ano}.csv'

pasta = 'dados/brutos'
os.makedirs(pasta, exist_ok=True)

for url in [url_votos, url_votacoes]:
    nome_arquivo = url.split('/')[-1]
    caminho_arquivo = os.path.join(pasta, nome_arquivo)

    if not os.path.exists(caminho_arquivo):
        print(f'Baixando {nome_arquivo}...')
        response = requests.get(url)
        with open(caminho_arquivo, 'wb') as f:
            f.write(response.content)
    else:
        print(f'{nome_arquivo} já existe. Pulando download.')