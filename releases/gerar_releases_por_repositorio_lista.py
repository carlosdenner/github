import json
import datetime
from datetime import timedelta
from dateutil import parser

def ler_arquivo_json_tipo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))


#================================================================================#
# MAIN                                                                           #
#================================================================================#

print("Informe o nome do arquivo.json das releases: ")
nome_arquivo_releases = input()

arquivo_json = ler_arquivo_json_tipo(nome_arquivo_releases)

repo_id_ant = 0

lista_releases = []

arquivos_json_saida = []

for i in range(len(arquivo_json)):
    lista_releases = []
    lista_releases = arquivo_json[i]['lista_releases']

    if len(lista_releases) == 0:
        registro = {}
        registro['id']   = arquivo_json[i]['id']
        registro['data'] = ""
        registro['quantidade_releases'] = 0
        arquivos_json_saida.append(registro)
    else:
        for x in range(len(lista_releases)):
            registro = {}
            registro['id']                  = arquivo_json[i]['id']
            registro['data']                = lista_releases[x]['data']
            registro['quantidade_releases'] = lista_releases[x]['quantidade_releases']
            arquivos_json_saida.append(registro)


nome_arquivo_releases_saida = f'saida-{str(nome_arquivo_releases)}'

gravar_arquivo_json(nome_arquivo_releases_saida,arquivos_json_saida)
