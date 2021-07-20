import json
import datetime
from dateutil import parser

def ler_arquivo_json_tipo_1(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

def gerar_data_criacao_repositorio(arquivo, arquivo_estrelas):
    repo_id_ant = 0

    for i in range(len(arquivo_estrelas)):

        if arquivo_estrelas[i]['repo_id'] != repo_id_ant:
            print(arquivo_estrelas[i]['repo_id'] )
            repo_id_ant =  arquivo_estrelas[i]['repo_id'] 

            registro = list(filter(lambda x:x["id"] == arquivo_estrelas[i]['repo_id'],arquivo))

            data_criacao_utc = registro[0]['created_at']
            data_criacao     = parser.parse(data_criacao_utc)
            data_criacao     = datetime.datetime.strftime(data_criacao, "%d-%m-%Y")
            arquivo_estrelas[i]['data_criacao'] = data_criacao
        else:
            arquivo_estrelas[i]['data_criacao'] = ""


    return arquivo_estrelas

#================================================================================#
# MAIN                                                                           #
#================================================================================#

print("Informe o arquivo.json dos repositórios: ")
nome_arquivo_repositorios = input()

print("Informe o nome do arquivo.json das estrelas: ")
nome_arquivo_estrelas = input()

arquivo_json_repositorios = ler_arquivo_json_tipo_1(nome_arquivo_repositorios)

arquivo_json_estrelas = ler_arquivo_json_tipo_1(nome_arquivo_estrelas)

arquivo_json_estrelas_saida = gerar_data_criacao_repositorio(arquivo_json_repositorios,arquivo_json_estrelas)

nome_arquivo_saida = f'saida-1-{str(nome_arquivo_estrelas)}'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_estrelas_saida)