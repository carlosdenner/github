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

print('Informe o primeiro arquivo arquivo.json: ')
nome_primeiro_arquivo = input()

print('Informe o segundo arquivo arquivo.json: ')
nome_segundo_arquivo = input()

arquivo_json_primeiro = ler_arquivo_json(nome_primeiro_arquivo)
print(f'Tamanho do primeiro arquivo {str(len(arquivo_json_primeiro))}')

arquivo_json_segundo = ler_arquivo_json(nome_segundo_arquivo)
print(f'Tamanho do segundo arquivo {str(len(arquivo_json_segundo))}')

for i in range(len(arquivo_json_primeiro)):

    if arquivo_json_primeiro[i]['id'] != arquivo_json_segundo[i]['id'] or arquivo_json_primeiro[i]['data'] != arquivo_json_segundo[i]['data']:
        id = arquivo_json_primeiro[i]['id']
        data = arquivo_json_primeiro[i]['data']
        print("Registro divergente")
        print(f'Primeiro arquivo: ID: {str(id)} - DATA: {str(data)}')
        id = arquivo_json_segundo[i]['id']
        data = arquivo_json_segundo[i]['data']
        print(f'Segundo arquivo: ID: {str(id)} - DATA: {str(data)}')
        break



