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
    print(arquivo_json[i]['name'])

    lista_releases = arquivo_json[i]['releases']

    print(f'Quantidade de releases: {len(lista_releases)}')

    # Caso o repositorio não tenha release gera registro
    # com data em branco
    if len(lista_releases) == 0: 
        registro = {}
        registro['id']           = arquivo_json[i]['id']
        registro['name']         = arquivo_json[i]['name']
        registro['url']          = arquivo_json[i]['url']
        registro['created_at']   = arquivo_json[i]['created_at']
        registro['num_watchers'] = arquivo_json[i]['num_watchers']
        registro['data']         = ""
        arquivo_json_saida.append(registro)
    else:
        # Caso o repositorio tenha release gera registro para cada
        # release com sua data.
        # Ler decrementando, pois as releases estão em ordem
        # decrescente por data.
        for x in range(len(lista_releases)-1,-1,-1):
            # Considera a data de publicação igual a data de criação
            data_hora = parser.parse(lista_releases[x]['published_at'])
            data      = datetime.datetime.strftime(data_hora, "%d-%m-%Y")

            registro = {}
            registro['id']           = arquivo_json[i]['id']
            registro['name']         = arquivo_json[i]['name']
            registro['url']          = arquivo_json[i]['url']
            registro['created_at']   = arquivo_json[i]['created_at']
            registro['num_watchers'] = arquivo_json[i]['num_watchers']
            registro['data']         = data
            arquivo_json_saida.append(registro)

nome_arquivo_saida = f'repositorio-release-data.json'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_saida)