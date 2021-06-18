import requests
import json
from datetime import datetime
from datetime import date
import time

def requisicao_api(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return resposta.status_code

def requisicao_url(url):
    dados_api = requisicao_api(url)
    return dados_api

def monta_quesitos_palavras_chave(lista_palavras_chaves):
    texto_quesitos = ''

    for x in range(len(lista_palavras_chaves)):
        if str(texto_quesitos) == '':
            texto_quesitos = str(lista_palavras_chaves[x]['palavra-chave']) + ':' + lista_palavras_chaves[x]['valor-palavra-chave']
        else:
            texto_quesitos = str(lista_palavras_chaves[x]['palavra-chave']) + ':' + lista_palavras_chaves[x]['valor-palavra-chave'] + '+' + str(texto_quesitos)
    
    return texto_quesitos

def monta_lista_repos_topico(quesito_pesquisa,lista_palavras_chave):
    lista_registros = []
    
    # Percorre os 1000 primeiros registros, ou seja, 10 páginas de 100 registros.
    for x in range(1,11):
        urlprincipal = f'https://api.github.com/search/repositories?q={str(quesito_pesquisa)}&sort=stars&order=desc&page={str(x)}&per_page=100' 

        dados_api = requisicao_url(urlprincipal)    

        if type(dados_api) is int: # Caso ocorra algum erro, finaliza busca
            print("Erro: " + str(dados_api))
            break
        else:
            print("Página: " + str(x))
            print(urlprincipal)

            items = dados_api['items']
            
            if len(items) == 0: #Verifica se lista está vazia e finaliza busca
                break
            else:
                #Pega os repositórios no item e insere em uma lista
                for i in range(len(items)):
                    lista_topicos = []

                    for y in range(len(lista_palavras_chave)): # Inclui na lista de tópicos somente os valores de palavras chaves de topico
                        if lista_palavras_chave[y]['palavra-chave'] == 'topic':
                            lista_topicos.append(lista_palavras_chave[y]['valor-palavra-chave'])

                    items[i]['lista_topicos'] = lista_topicos
                    lista_registros.append(items[i])
        
    return(lista_registros)


def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

#================================================================================#
# MAIN                                                                           #
#================================================================================#
print("Deseja pesquisar por quais quesitos (palavras-chave):")

fim_palavras_chave = 'S'
y = 0
lista_palavras_chave = []

while fim_palavras_chave == 'S': 
    y = y + 1
    palavra_chave = {}
    
    print(f'{str(y)}ª palavra-chave: ')
    palavra_chave['palavra-chave'] = input().replace(" ","").lower() 

    print(f'Valor da {str(y)}ª palavra-chave: ')
    palavra_chave['valor-palavra-chave'] = input().replace(" ","").lower() 

    lista_palavras_chave.append(palavra_chave)

    print("Deseja continuar (S,N): ")
    fim_palavras_chave = input()

    while fim_palavras_chave != 'N' and fim_palavras_chave != 'S':
        print("Erro ! - Informar S ou N !")
        print("Deseja continuar (S,N): ")
        fim_palavras_chave = input()

# Monta quesito de pesquisa com as palavras chaves indicadas
quesito_pesquisa = monta_quesitos_palavras_chave(lista_palavras_chave)

# Monta uma lista com os repositórios do tópico
lista_repos = monta_lista_repos_topico(quesito_pesquisa,lista_palavras_chave)

# Monta um json com tópico e lista de repositórios
registro_json           = {}

registro_json['items']  = lista_repos
arquivo_json            = registro_json

# Busca data e hora atual
data_hora_atual = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

nome_arquivo = f'{str(quesito_pesquisa)}-{str(data_hora_atual)}.json' 

# Grava json
gravar_arquivo_json(nome_arquivo, arquivo_json)