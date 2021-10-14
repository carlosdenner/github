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

print('Informe o nome do arquivo.json: ')
nome_arquivo = input()

arquivo_json = ler_arquivo_json(nome_arquivo)

arquivo_json_saida = []

for i in range(len(arquivo_json)):
    if arquivo_json[i]['data'] == '31-05-2019' and arquivo_json[i]['releases'] == 0:
        arquivo_json_saida.append(arquivo_json[i])

nome_arquivo_saida = f'saida-{str(nome_arquivo)}'

print(f'Quantidade de repositórios sem releases: {str(len(arquivo_json_saida))}.')

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_saida)