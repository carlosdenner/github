import requests
import json
import time 

def requisicao_api(url,headers):
    resposta = requests.get(url,headers=headers)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return resposta.status_code

def ler_arquivo_json(nome_arquivo):
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



print("Informe o nome do arquivo.json que deseja consultar os topicos: ")
nome_arquivo = input()

arquivo_json = ler_arquivo_json(nome_arquivo)

arquivo_json_topicos = consulta_topicos(arquivo_json)

# gravar_arquivo_json('teste-topicos.json' , arquivo_json_topicos)