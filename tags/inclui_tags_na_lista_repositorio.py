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
print(f'tamanho: {str(tamanho)}')
while x < tamanho:

    if int(arquivo_json_tags[x]['id']) == 78029:
        print("ACHOU !")
        print(arquivo_json_tags[x])
        print(arquivo_json_releases[i])

    if int(arquivo_json_tags[x]['id']) == 82809:
        print("ACHOU !")
        print(arquivo_json_tags[x])
        print(arquivo_json_releases[i])
    print(f'x: {str(x)}')
    print(f'i: {str(i)}')
    print(arquivo_json_tags[x]['id'])
    print(arquivo_json_releases[i]['id'])
    if arquivo_json_tags[x]['id'] == arquivo_json_releases[i]['id'] and arquivo_json_tags[x]['data'] != "":
        lista_releases = []
        lista_releases = arquivo_json_releases[i]['lista_releases']

        #print(f'Tamanho lista: {str(len(lista_releases))}')

        if primeiro:
            # Transforma toda a lista em date time
            for z in range(len(lista_releases)):
                #print(type(lista_releases[z]['data']))
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

print("aqui")
for x in range(len(arquivo_json_releases)):
    print(arquivo_json_releases[x]['id'])
    lista_releases = arquivo_json_releases[x]['lista_releases']
    #print(f'x1: {str(x)}')
    for i in range(len(lista_releases)):
        print(lista_releases[i])
        lista_releases[i]['data'] = datetime.datetime.strftime(lista_releases[i]['data'], "%d-%m-%Y")

    arquivo_json_releases[x]['lista_releases'] = lista_releases

print("aqui2")
nome_arquivo_saida = f'tags-data-{str(arquivo_json_releases)}'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_releases)