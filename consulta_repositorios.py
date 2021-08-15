import requests
import json
from datetime import datetime
import time 

def requisicao_api(url,headers):
    resposta = requests.get(url,headers=headers)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return resposta.status_code

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

        headers = {'Accept': 'application/vnd.github.mercy-preview+json', 'Accept-Charset': 'UTF-8'}

        dados_api = requisicao_api(urlprincipal,headers)    

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
                    lista_registros.append(items[i])
        
    return(lista_registros)

# Busca os 10 tópicos mais populares que tem a palavra data em algum de suas descrições
def busca_exemplos_topicos():
    url = "https://api.github.com/search/topics?q=data&page=1&per_page=10"

    headers = {'Accept': 'application/vnd.github.mercy-preview+json', 'Accept-Charset': 'UTF-8'}

    resultado = requisicao_api(url, headers) 

    lista_topicos = resultado['items']

    exemplos_topicos = ''

    # Monta string de exemplos
    for x in range(len(lista_topicos)):
        if exemplos_topicos == '':
           exemplos_topicos = str(lista_topicos[x]['name'])
        else:
            exemplos_topicos = exemplos_topicos + " , "  + str(lista_topicos[x]['name'])
    
    return exemplos_topicos


def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

#================================================================================#
# MAIN                                                                           #
#================================================================================#
print("Consulta Repositórios")

fim_palavras_chave = 'S'
y = 0
lista_palavras_chave = []

#exemplos_topicos = busca_exemplos_topicos()
exemplos_topicos = ' ' 

# Recebe todas as palavras-cheve e seus valores 
while fim_palavras_chave == 'S': 
    y = y + 1
    palavra_chave = {}
    
    print(f'{str(y)}ª palavra-chave (Exemplo: topic): ')
    palavra_chave['palavra-chave'] = input().replace(" ","").lower() # sempre deixa palavra-chave sem espaço e minuscula

    if (palavra_chave['palavra-chave'] == 'topic'):
        print(f'Valor da {str(y)}ª palavra-chave (Exemplos: {exemplos_topicos}): ')
    else:
        print(f'Valor da {str(y)}ª palavra-chave: ')

    palavra_chave['valor-palavra-chave'] = input()

    lista_palavras_chave.append(palavra_chave)

    print("Deseja continuar (S,N): ")
    fim_palavras_chave = input()

    while fim_palavras_chave != 'N' and fim_palavras_chave != 'S':
        print("Erro ! - Informar S ou N !")
        print("Deseja continuar (S,N): ")
        fim_palavras_chave = input()

# Espera 1 minuto para não ocorrer problemas nas requisiçõess
#print("Carregando... Espere 1 minuto.")
#time.sleep(60)

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