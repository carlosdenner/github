import requests
import json
import csv

def requisicao_api(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return resposta.status_code

def imprime_repositorios(self):
    dados_api = self.requisicao_api()
    if type(dados_api) is not int:
        for i in range(len(dados_api)):
            print(dados_api[i]['name'])
    else:
        print(dados_api)

urlprincipal = 'https://api.github.com/search/repositories?q=topic:data-science&sort=stars&order=desc&page=1&per_page=100'
dados_api = requisicao_api(urlprincipal)


print(dados_api['total_count'])
items = dados_api['items']

arquivo = open("arquivo.txt", 'r+')
texto = arquivo.readlines()

for i in range(len(items)):
    textolinha = str(items[i]['name']) + ";" + str(items[i]['stargazers_count'])  + "\t\n"
    texto.append(textolinha)
    print(items[i]['full_name'])
    print(items[i]['stargazers_count'])
    print(items[i]['language'])
    print(items[i]['created_at'])

arquivo.writelines(texto)
arquivo.close()
