import requests
import json
from datetime import datetime

def requisicao_api(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return resposta.status_code

def requisicao_url(url):
    dados_api = requisicao_api(url)
    return dados_api

def monta_lista_repos_topico(topico):
    lista_registros = []
    
    # Percorre os 1000 primeiros registros, ou seja, 10 páginas de 100 registros.
    for x in range(1,11):
        urlprincipal = f'https://api.github.com/search/repositories?q=topic:{str(topico)}&sort=stars&order=desc&page={str(x)}&per_page=100' 

        dados_api = requisicao_url(urlprincipal)    

        if type(dados_api) is int: # Caso ocorra algum erro. Sai do loop e retorna lista vazia
            print("Erro: " + str(dados_api))
            break
        else:
            #Pega os repositórios no item e insere em uma lista
            print("Página: " + str(x))
            print(urlprincipal)

            items = dados_api['items']
    
            for i in range(len(items)):
                lista_topicos = [topico]
                items[i]['lista_topicos'] = lista_topicos
                lista_registros.append(items[i])
        
    return(lista_registros)


def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

#================================================================================#
# MAIN                                                                           #
#================================================================================#
print("Deseja pesquisar por quais quesitos (palavras-chave):")

#fim_palavras_chave = 0
#y = 'N'
#lista_palavras_chave = []

#while fim_palavras_chave == 'N': 
#    y = y + 1
#    print(y + "ª palavra-chave: ")
#    lista_palavras_chave[y]= input()
#    print("Valor da " +  y + "ª palavra-chave: ")
#
#    print("Deseja continuar (S,N): ")


topico = 'opendata'
# Monta uma lista com os repositórios do tópico
lista_repos = monta_lista_repos_topico(topico)

# Monta um json com tópico e lista de repositórios
registro_json           = {}

registro_json['items']  = lista_repos
arquivo_json            = registro_json

data_hora_atual = datetime.now()

nome_arquivo = str(topico) + "-" + str(data_hora_atual) + ".json" 

# Grava json
gravar_arquivo_json(nome_arquivo, arquivo_json)

# Leitura json
json_leitura = ler_arquivo_json(nome_arquivo)
