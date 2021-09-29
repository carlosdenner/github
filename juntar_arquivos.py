import json
import datetime
from dateutil import parser

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

#================================================================================#
# MAIN                                                                           #
#================================================================================#

print('Informe o arquivo.json de estrelas: ')
nome_arquivo_estrelas = input()

print('Informe o arquivo.json de forks: ')
nome_arquivo_forks = input()

print('Informe o arquivo.json de releases: ')
nome_arquivo_releases = input()

print('Informe o arquivo.json de code frequency: ')
nome_arquivo_code_frequency = input()

arquivo_json_estrelas = ler_arquivo_json(nome_arquivo_estrelas)
print(f'Tamanho do arquivo estrelas: {str(len(arquivo_json_estrelas))}')

arquivo_json_forks = ler_arquivo_json(nome_arquivo_forks)
print(f'Tamanho do arquivo forks {str(len(arquivo_json_forks))}')

arquivo_json_releases = ler_arquivo_json(nome_arquivo_releases)
print(f'Tamanho do arquivo releases {str(len(arquivo_json_releases))}')

arquivo_json_code_frequency = ler_arquivo_json(nome_arquivo_code_frequency)
print(f'Tamanho do arquivo code frequency {str(len(arquivo_json_code_frequency))}')

arquivo_json_saida = []

# Juntar estrelas com forks
for i in range(len(arquivo_json_estrelas)):

    registro = {}
    registro['id']               = arquivo_json_estrelas[i]['id']
    registro['data']             = arquivo_json_estrelas[i]['data']
    registro['estrelas']         = arquivo_json_estrelas[i]['estrelas']
    registro['forks']            = arquivo_json_forks[i]['forks']
    registro['releases']         = arquivo_json_releases[i]['releases']
    registro['linhas_alteradas'] = arquivo_json_code_frequency[i]['linhas_alteradas']
    arquivo_json_saida.append(registro)

print(f'Quantidade de registros de saida: {str(len(arquivo_json_saida))}')

nome_arquivo_saida = f'historico-geral-de-indicadores.json'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_saida)