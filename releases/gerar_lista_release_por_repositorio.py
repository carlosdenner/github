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

    if arquivo_json[i]['id'] != repo_id_ant or i == 0:
        registro       = {}

        if i == 0:
            registro['id'] = int(arquivo_json[i]['id'])
        else:
            registro['id'] = int(repo_id_ant)
            repo_id_ant    = arquivo_json[i]['id']

        registro['lista_releases'] = lista_releases
        arquivos_json_saida.append(registro)
        lista_releases = []
        

    if arquivo_json[i]['data'] != "":
        registro = {}   
        registro['data'] = arquivo_json[i]['data']
        registro['quantidade_releases'] = arquivo_json[i]['quantidade_releases']
        lista_releases.append(registro)

registro = {}
registro['id'] = int(repo_id_ant)
registro['lista_releases'] = lista_releases
arquivos_json_saida.append(registro)  

nome_arquivo_releases_saida = f'saida-{str(nome_arquivo_releases)}'

gravar_arquivo_json(nome_arquivo_releases_saida,arquivos_json_saida)
