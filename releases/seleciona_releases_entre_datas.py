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

for i in range(len(arquivo_json)):

    lista_releases_saida = []

    lista_releases = arquivo_json[i]['releases']
    
    for x in range(len(lista_releases)):

        data_hora      = parser.parse(lista_releases[x]['published_at'])
        data           = datetime.datetime.strftime(data_hora, "%d-%m-%Y")
        dataformatdate = datetime.datetime.strptime(data, "%d-%m-%Y")

        print(dataformatdate)
        
        datainicio = datetime.datetime.strptime('01-02-2012' , "%d-%m-%Y")
        datafim    = datetime.datetime.strptime('01-06-2019' , "%d-%m-%Y")

        if dataformatdate >= datainicio and dataformatdate < datafim:
            lista_releases_saida.append(lista_releases[x])
        else:
            print("Release não está entre o período definido!")

    registro = {}
    registro['id']           = arquivo_json[i]['id']
    registro['name']         = arquivo_json[i]['name']
    registro['url']          = arquivo_json[i]['url']
    registro['created_at']   = arquivo_json[i]['created_at']
    registro['num_watchers'] = arquivo_json[i]['num_watchers']
    registro['releases']     = lista_releases_saida
    arquivo_json_saida.append(registro)

nome_arquivo_saida = f'entre-datas-{nome_arquivo}'
gravar_arquivo_json(nome_arquivo_saida,arquivo_json_saida)