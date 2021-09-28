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

print('Informe o arquivo.json de code frequency: ')
nome_arquivo = input()

print('Informe o arquivo.json de repositorios: ')
nome_arquivo_repositorios = input()

arquivo_json = ler_arquivo_json(nome_arquivo)

arquivo_json_repo = ler_arquivo_json(nome_arquivo_repositorios)

repo_id_ant = 0
data_criacao = ""

arquivo_json_saida = []

for i in range(len(arquivo_json)):

    if repo_id_ant != arquivo_json[i]['id']:

        repo_id_ant      = arquivo_json[i]['id']

        for x in range(len(arquivo_json_repo)):
            if arquivo_json[i]['id'] == arquivo_json_repo[x]['id']:
                data_criacao_ant = arquivo_json_repo[x]['created_at']
                data_hora        = parser.parse(data_criacao_ant)
                data             = datetime.datetime.strftime(data_hora, "%d-%m-%Y")
                data_criacao     = datetime.datetime.strptime(data, "%d-%m-%Y")

    data_hora_reg  = parser.parse(arquivo_json[i]['data'])
    data_reg       = datetime.datetime.strftime(data_hora_reg, "%d-%m-%Y")
    data_reg       = datetime.datetime.strptime(data_reg, "%d-%m-%Y")

    if data_criacao > data_reg:
        print(f'Data menor: {str(data_reg)}') 
    else:
        arquivo_json_saida.append(arquivo_json[i])

nome_arquivo_saida = f'saida-{str(nome_arquivo)}'

print(f'Quantidade de registros {str(len(arquivo_json_saida))}')

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_saida)