import json
import datetime
from dateutil import parser

def ler_arquivo_json_tipo_1(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)


def gerar_data_criacao_repositorio(arquivo, arquivo_2):
    repo_id_ant = 0

    for i in range(len(arquivo_2)):
        
        if arquivo_2[i]['id'] != repo_id_ant:
            repo_id_ant =  str(arquivo_2[i]['id'])

            registro = list(filter(lambda x:x["id"] == arquivo_2[i]['id'],arquivo))
            
            data_criacao_utc = registro[0]['created_at']
            data_criacao     = parser.parse(data_criacao_utc)
            data_criacao     = datetime.datetime.strftime(data_criacao, "%d-%m-%Y")
            arquivo_2[i]['data_criacao'] = data_criacao
        else:
            arquivo_2[i]['data_criacao'] = ""


    return arquivo_2

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

#================================================================================#
# MAIN                                                                           #
#================================================================================#

print("Informe o arquivo.json dos repositórios: ")
nome_arquivo_repositorios = input()

print("Informe o nome do arquivo.json: ")
nome_arquivo = input()

arquivo_json_repositorios = ler_arquivo_json_tipo_1(nome_arquivo_repositorios)

arquivo_json = ler_arquivo_json_tipo_1(nome_arquivo)

arquivo_json_saida = gerar_data_criacao_repositorio(arquivo_json_repositorios,arquivo_json)

nome_arquivo_saida = f'saida-1-{str(nome_arquivo)}'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_saida)