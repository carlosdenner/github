import pandas as pd
import json
import csv

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))


print("Informe o arquivo.csv: ")
nome_arquivo = input()

arquivo_json = []

with open(nome_arquivo) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        registro = {}
        registro['id']                    = int(rows['id'])
        registro['name']                  = rows['name']
        registro['url']                   = rows['url']
        registro['created_at']            = rows['created_at']
        registro['num_watchers']          = rows['num_watchers']
        if str(rows['data']) == "nan":
            registro['data']              = ""
        else:
            registro['data']              = rows['data']
        
        registro['quantidade_releases']   = int(rows['quantidade_releases'])
        arquivo_json.append(registro)
        
nome_arquivo = nome_arquivo.replace('csv','json')

print(f'Quantidade de registros de saida: {str(len(arquivo_json))}')

gravar_arquivo_json(nome_arquivo,arquivo_json)