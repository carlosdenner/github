import json
import datetime
import operator
from datetime import timedelta
from dateutil import parser

def diferenca_entre_datas(data1, data2):
    d1 = datetime.datetime.strptime(data1, "%d-%m-%Y")
    d2 = datetime.datetime.strptime(data2, "%d-%m-%Y")
    return abs((d1 - d2).days)

def ler_arquivo_json_tipo_1(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

# Gerar lista de repositorios desde sua data de criacao até uma data limite com estrelas zeradas
def gerar_datas_repositorios_criacao_ate_fim(arquivo_json):
    arquivo_saida = []

    for i in range(len(arquivo_json)):
        
        # Formata a data de criação do repositório
        data_criacao_utc = arquivo_json[i]['created_at']
        data_criacao = parser.parse(data_criacao_utc)
        data_criacao = datetime.datetime.strftime(data_criacao, "%d-%m-%Y")
        
        # Calcula a diferença entre a data de criação e a data limite
        qtd_dias = diferenca_entre_datas(data_criacao,'01-06-2019')
        
        data_hora = parser.parse(data_criacao)
        
        # Cria registro para todas as datas entre a data de criação
        # e a data limite informando número de estrelas zerado
        for x in range(qtd_dias):
            data_hora = data_hora + timedelta(days=1)
            data = datetime.datetime.strftime(data_hora, "%d-%m-%Y")
            registro = {}
            registro['id']       = arquivo_json[i]['id']
            registro['data']     = data
            registro['estrelas'] = 0
            arquivo_saida.append(registro)
            
    return arquivo_saida

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

#================================================================================#
# MAIN                                                                           #
#================================================================================#

print("Informe o arquivo.json dos repositórios: ")
nome_arquivo_repositorios = input()

arquivo_json = ler_arquivo_json_tipo_1(nome_arquivo_repositorios)

arquivo_json_saida = gerar_datas_repositorios_criacao_ate_fim(arquivo_json)

nome_arquivo_repositorios_saida = f'saida-{str(nome_arquivo_repositorios)}'

gravar_arquivo_json(nome_arquivo_repositorios_saida,arquivo_json_saida)