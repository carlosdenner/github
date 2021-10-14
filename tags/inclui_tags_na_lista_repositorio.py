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

print('Informe o arquivo.json das tags: ')
nome_arquivo_tags = input()

print('Informe o arquivo.json das releases: ')
nome_arquivo_releases = input()


arquivo_json_tags = ler_arquivo_json(nome_arquivo_tags)

arquivo_json_releases = ler_arquivo_json(nome_arquivo_releases)

i = 0

primeiro = True
tamanho = int(len(arquivo_json_tags))
x = 0

while x < tamanho:

    if arquivo_json_tags[x]['id'] == arquivo_json_releases[i]['id'] and arquivo_json_tags[x]['data'] != "":
        lista_releases = []
        lista_releases = arquivo_json_releases[i]['lista_releases']


        if primeiro:
            # Transforma toda a lista em date time
            for z in range(len(lista_releases)):
                data = datetime.datetime.strptime(lista_releases[z]['data'], "%d-%m-%Y")
                lista_releases[z]['data'] = data
        
        primeiro = False
        achou = False

        # Procura se data já existe e adiciona mais uma ocorrência no somatório do dia
        for z in range(len(lista_releases)):
            if arquivo_json_tags[x]['data'] == lista_releases[z]['data']:
                lista_releases[z]['quantidade_releases'] = int(lista_releases[z]['quantidade_releases']) + 1
                achou = True
                break
        
        # Caso a data não exista: cria registro na lista e ordena pela data
        if not achou:
            data = datetime.datetime.strptime(arquivo_json_tags[x]['data'], "%d-%m-%Y")
            registro = {} 
            registro['data'] = data
            registro['quantidade_releases'] = int(1)
            lista_releases.append(registro)
            lista_releases.sort(key=lambda item:item['data'], reverse=False)

        arquivo_json_releases[i]['lista_releases'] = lista_releases
        x = x + 1 
    else:
        primeiro = True
        i = i + 1

        if arquivo_json_tags[x]['data'] == "":
            x = x + 1

            lista_releases = []
            lista_releases = arquivo_json_releases[i]['lista_releases']

            # Transforma toda a lista em date time
            for z in range(len(lista_releases)):
                data = datetime.datetime.strptime(lista_releases[z]['data'], "%d-%m-%Y")
                lista_releases[z]['data'] = data

            arquivo_json_releases[i]['lista_releases'] = lista_releases

for x in range(len(arquivo_json_releases)):
    print(arquivo_json_releases[x]['id'])
    lista_releases = []
    lista_releases = arquivo_json_releases[x]['lista_releases']

    for i in range(len(lista_releases)):
        data = datetime.datetime.strftime(lista_releases[i]['data'], "%d-%m-%Y")
        lista_releases[i]['data'] = data

    arquivo_json_releases[x]['lista_releases'] = lista_releases

#arquivo_json_releases_saida = []

#for x in range(999,1000):
#    print(arquivo_json_releases[x])
#    arquivo_json_releases_saida.append(arquivo_json_releases[x])

nome_arquivo_saida = 'tags-releases.json'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_releases)