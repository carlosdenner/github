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
# Objetivo: retirar todos os registros antes da criação do repositório.          #
#================================================================================#

print('Informe o arquivo.json com os registros: ')
nome_arquivo = input()

print('Informe o arquivo.json dos repositórios: ')
nome_arquivo_repo = input()

arquivo_json      = ler_arquivo_json(nome_arquivo)
arquivo_json_repo = ler_arquivo_json(nome_arquivo_repo)

repo_id_ant = 0

arquivo_json_saida = []

print(f'Tamanho do arquivo de entrada: {len(arquivo_json)}')

for i in range(len(arquivo_json)):

    if arquivo_json[i]['id'] != repo_id_ant:
        repo_id_ant = arquivo_json[i]['id'] 
        
        for x in range(len(arquivo_json_repo)):
            if arquivo_json_repo[x]['id'] == repo_id_ant:
                data_hora = parser.parse(arquivo_json_repo[x]['created_at'])
                data      = datetime.datetime.strftime(data_hora, "%d-%m-%Y")
                
    data1 = datetime.datetime.strptime(arquivo_json[i]['data'], "%d-%m-%Y")
    data2 = datetime.datetime.strptime(data, "%d-%m-%Y")

    if data1 < data2:
        print(f'Retirado -> Repositório {repo_id_ant} - Data registro {data1} - Data criação repositório {data2}')
    else:
        arquivo_json_saida.append(arquivo_json[i])

print(f'Tamanho do arquivo de entrada: {len(arquivo_json_saida)}')

nome_arquivo_saida = f'saida-{nome_arquivo}'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_saida)