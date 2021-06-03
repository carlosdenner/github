import requests
import json

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

        print(urlprincipal)

        dados_api = requisicao_url(urlprincipal)    

        if type(dados_api) is int: # Caso ocorra algum erro. Sai do loop e retorna lista vazia
            print("Erro: " + str(dados_api))
            break
        else:
            #Pega os repositórios no item e insere em uma lista
            print("Página: " + str(x))

            items = dados_api['items']
    
            for i in range(len(items)):
                lista_registros.append(items[i])
        
    return(lista_registros)


def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

#================================================================================#
# MAIN                                                                           #
#================================================================================#

# Alterar essas duas variáveis
topico       = "open-data"
nome_arquivo = "open-data.json"

# Monta uma lista com os repositórios do tópico
lista_repos = monta_lista_repos_topico(topico)

# Monta um json com tópico e lista de repositórios
registro_json           = {}
registro_json['topico'] = topico
registro_json['item']   = lista_repos
registro_json_1 = json.dumps(registro_json, indent=2, sort_keys=False)

print(registro_json_1)

# Grava json
gravar_arquivo_json(nome_arquivo, registro_json_1)