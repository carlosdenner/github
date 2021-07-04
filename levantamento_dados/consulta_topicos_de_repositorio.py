import requests
import json
import time 

def requisicao_api(url,headers):
    resposta = requests.get(url,headers=headers)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return resposta.status_code

def ler_arquivo_json_tipo_1(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def ler_arquivo_json_tipo_2(nome_arquivo):
    lista_json = []
    for line in open(nome_arquivo, 'r', encoding='utf8'):
        lista_json.append(json.loads(line))

    return lista_json


def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

def consulta_topicos(lista_repositorios):
    lista_parcial = []
    
    for i in range(0,10):
        print(lista_repositorios[i]['url'])
        urlprincipal = str(lista_repositorios[i]['url']) + '/topics'
        headers = {'Accept': 'application/vnd.github.mercy-preview+json', 'Accept-Charset': 'UTF-8'}
        dados_api = requisicao_api(urlprincipal,headers)
        print(dados_api)
        if type(dados_api) is int: # Caso ocorra algum erro.
            if dados_api == 404: # Página de topicos não encontrada então deixa lista vazia
                print(dados_api)
                lista_repositorios[i]['list_topics'] = []
                lista_parcial.append(lista_repositorios[i])
            else:
                if dados_api == 403:
                    gravar_arquivo_json('teste-topicos.json' , lista_parcial)
                    time.sleep(60)
                else:
                    print("Erro: " + str(dados_api))
                    break
        else:
            print(dados_api)
            lista_repositorios[i]['list_topics'] = dados_api['names']
            lista_parcial.append(lista_repositorios[i])

    return lista_repositorios

# Verifica se o repositorio está na base de dados json. Em caso positivo, atribui a lista de topicos.
def consulta_topicos_base_de_dados_json(base_dados_json, arquivo_json):
    arquivo_json_topicos = []

    for i in range(len(arquivo_json)):
        for x in range(len(base_dados_json)):
            if arquivo_json[i]['url'] == base_dados_json[x]['url']:
                arquivo_json[i]['list_topics'] = base_dados_json[x]['topics']
                arquivo_json_topicos.append(arquivo_json[i])
                break
    
    return arquivo_json_topicos

        
#================================================================================#
# MAIN                                                                           #
#================================================================================#

nome_base_dados = "base_dados_repositorios.json"

print("Informe o nome do arquivo.json que deseja consultar os topicos: ")
nome_arquivo = input()

arquivo_json = ler_arquivo_json_tipo_2(nome_arquivo)
base_dados = ler_arquivo_json_tipo_1(nome_base_dados)
base_dados_json = base_dados['items']

arquivo_json_topicos = consulta_topicos_base_de_dados_json(base_dados_json, arquivo_json)

gravar_arquivo_json('teste_topicos.json', arquivo_json_topicos)