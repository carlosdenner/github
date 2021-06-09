import requests
import json
from time import sleep

fim = 0

def requisicao_api(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return resposta.status_code

def requisicao_url(url):
    dados_api = requisicao_api(url)
    return dados_api

def monta_lista_repos_topico(lista_registros, topico, timestamp):    
    global fim 
    # Percorre os 1000 primeiros registros, ou seja, 10 páginas de 100 registros.
    for x in range(1,11):
        urlprincipal = f'https://api.github.com/search/repositories?q=topic:{str(topico)}+pushed:<{str(timestamp)}&sort=pushed&order=desc&page={str(x)}&per_page=100' 
        
        dados_api = requisicao_url(urlprincipal)    

        if type(dados_api) is int: # Caso ocorra algum erro. Sai do loop e retorna lista vazia
            print("Erro: " + str(dados_api))
            break
        else:

            items = dados_api['items']

            if len(items) == 0:
                print("Fim")
                fim = 1
                break
            else:
                #Pega os repositórios no item e insere em uma lista
                print("Página: " + str(x))
                print(urlprincipal)
    
                for i in range(len(items)):
                    lista_registros.append(items[i])
        
    return(lista_registros)


def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def remove_duplicidade_lista(lista):

    i = 0
    while i < len(lista):
        j = i + 1
        registro_pesquisa = lista[i]['id']
        while j < len(lista):
            if registro_pesquisa == lista[j]['id']:
                lista.pop(j)
            else:
                j = j + 1
        i = i + 1

    return lista

#================================================================================#
# MAIN                                                                           #
#================================================================================#

# Alterar essas duas variáveis
topico       = "opendata"
nome_arquivo = "opendata.json"


lista_registros = []
timestamp = '2970-12-31T23:59:59Z'

sair = 0

while sair != 1:
    sleep(60)

    # Monta uma lista com os repositórios do tópico
    lista_repos = monta_lista_repos_topico(lista_registros,topico,timestamp)

    if fim == 1:
        sair = 1
    else:
        ultimo_registro = lista_repos[len(lista_repos) - 1]
    
        timestamp = ultimo_registro['pushed_at']

        print(timestamp)

print(len(lista_repos))

lista_sem_duplicados = remove_duplicidade_lista(lista_repos)

print(len(lista_sem_duplicados))

# Monta um json com tópico e lista de repositórios
registro_json           = {}
registro_json['topico'] = topico

registro_json['items']  = lista_repos
arquivo_json            = registro_json

# Grava json
gravar_arquivo_json(nome_arquivo, arquivo_json)


# Leitura json
#json_leitura = ler_arquivo_json(nome_arquivo)