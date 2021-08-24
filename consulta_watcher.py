import requests
import json

def requisicao_api(url,headers):
    resposta = requests.get(url,headers=headers)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return resposta.status_code

url = 'https://api.github.com/repos/django/django/subscription'
header = {
        'Authorization' : 'token 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',
        'Accept': 'application/vnd.github.mercy-preview+json', 
        'Accept-Charset': 'UTF-8'
        }

dados = requisicao_api(url,header)

print(dados)