import json
import datetime
from dateutil import parser

def ler_arquivo_json_tipo_2(nome_arquivo):
    lista_json = []
    for line in open(nome_arquivo, 'r', encoding='utf8'):
        lista_json.append(json.loads(line))
    
    return lista_json

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

print("Informe nome do arquivo: ")
nome_arquivo = input()

arquivo_json = ler_arquivo_json_tipo_2(nome_arquivo)

for i in range(len(arquivo_json)):

    data_hora = parser.parse(arquivo_json[i]['created_at'])
    data = datetime.datetime.strftime(data_hora, "%d-%m-%Y")
    arquivo_json[i]['created_at'] = data


nome_arquivo_saida = f'saida-{nome_arquivo}'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json)

