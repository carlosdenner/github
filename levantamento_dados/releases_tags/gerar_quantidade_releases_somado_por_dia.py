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

print('Informe o arquivo.json dos repositórios com suas releases: ')
nome_arquivo = input()

arquivo_json = ler_arquivo_json(nome_arquivo)

arquivo_json_saida = []

id_repo_ant = 0
data_repo_ant = ""
quantidade_releases = 0
repo_anterior = {}

for i in range(len(arquivo_json)):

    # Quando quebrar repositório grava registro anterior e sua quantidade de releases
    if arquivo_json[i]['id'] != id_repo_ant and bool(repo_anterior) == True:

        registro                 = {}
        registro['id']           = repo_anterior['id']
        registro['name']         = repo_anterior['name']
        registro['url']          = repo_anterior['url']
        registro['created_at']   = repo_anterior['created_at']
        registro['num_watchers'] = repo_anterior['num_watchers']

        # Caso o repositorio não tenha releases
        # Não define data e grava zero nas releases
        if data_repo_ant == "":
            registro['data']                = ""
            registro['quantidade_releases'] = 0
        else:
            quantidade_releases = quantidade_releases + 1
            registro['data']                = data_repo_ant
            registro['quantidade_releases'] = quantidade_releases

        arquivo_json_saida.append(registro)

        id_repo_ant   = arquivo_json[i]['id']
        data_repo_ant = arquivo_json[i]['data']
        quantidade_releases = 0

    else:
        # Quando quebrar data grava registro anterior e sua quantidade de releases 
        if arquivo_json[i]['data'] != data_repo_ant and bool(repo_anterior) == True: 
            registro                 = {}
            registro['id']           = repo_anterior['id']
            registro['name']         = repo_anterior['name']
            registro['url']          = repo_anterior['url']
            registro['created_at']   = repo_anterior['created_at']
            registro['num_watchers'] = repo_anterior['num_watchers']
            registro['data']         = data_repo_ant
            quantidade_releases = quantidade_releases + 1
            registro['quantidade_releases'] = quantidade_releases
                
            arquivo_json_saida.append(registro)
            
            id_repo_ant   = arquivo_json[i]['id']
            data_repo_ant = arquivo_json[i]['data']
            quantidade_releases = 0

        else:
            # Quando o repositório é o mesmo e a data é a mesma incrementa quantidade de releases
            quantidade_releases = quantidade_releases + 1

    repo_anterior = arquivo_json[i]
        


# Grava o último registro quando sai do loop
repo_anterior = arquivo_json[i]

registro                 = {}
registro['id']           = repo_anterior['id']
registro['name']         = repo_anterior['name']
registro['url']          = repo_anterior['url']
registro['created_at']   = repo_anterior['created_at']
registro['num_watchers'] = repo_anterior['num_watchers']
registro['data']         = data_repo_ant

if data_repo_ant == "":
    registro['data']                = ""
    registro['quantidade_releases'] = 0
else:
    quantidade_releases = quantidade_releases + 1
    registro['data']                = data_repo_ant
    registro['quantidade_releases'] = quantidade_releases

arquivo_json_saida.append(registro)



nome_arquivo_saida = f'quantidade-releases-somado-por-dia.json'

gravar_arquivo_json(nome_arquivo_saida, arquivo_json_saida)