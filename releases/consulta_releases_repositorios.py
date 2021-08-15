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
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def consulta_releases_repositorios(arquivo):
    arquivo_saida = []
    erro = False
    lista_releases = []
    existe_releases = False

    # Caso tenha problemas com conexão limite uma quantidade de registros
    # Retire os registros do arquivo de entrada que já estão no arquivo de saida
    # Caso não tenha coloque não tenha coloque o tamanho do arquivo.

    for x in (range(len(arquivo))):
        
        for i in range(1,11):

            url = arquivo[x]['url']
            urlprincipal = f'{str(url)}/releases?page={str(i)}&per_page=100' 

            # Caso o token expire. Basta acessar o link abaixo e criar um novo e inserir aqui.
            # https://docs.github.com/pt/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token
            headers = {
                'Authorization' : 'token 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',
                'Accept': 'application/vnd.github.mercy-preview+json', 
                'Accept-Charset': 'UTF-8'
                }

            dados_api = requisicao_api(urlprincipal,headers)    

            if type(dados_api) is int: # Caso ocorra algum erro, finaliza busca
                # 404 - Quando a página não é encontrada grava sem releases
                # 451 - Página bloqueada por motivos legais
                if dados_api == 404 or dados_api == 451: 
                    registro = {}
                    registro['id']           = arquivo[x]['id'] 
                    registro['name']         = arquivo[x]['name']
                    registro['url']          = arquivo[x]['url']
                    registro['created_at']   = arquivo[x]['created_at']
                    registro['num_watchers'] = arquivo[x]['num_watchers']       
                    registro['releases']     = [] 
                    arquivo_saida.append(registro)
                    break
                else:
                    if dados_api == 403: # Espera 90 segundos e continua processo:
                       print("ERRO 403 - Espere 90 segundos ...")
                       time.sleep(90) 
                       i = i - 1 # Decrementa o contador para fazer nova requisição
                    else: 
                        print("Erro: " + str(dados_api))
                        erro = True
                        break
            else:
                print("Página: " + str(i))
                print(urlprincipal)

                items = dados_api
                
                if len(items) == 0: #Verifica se lista está vazia e finaliza busca

                    if i == 1: # Grava o registro sem releases
                        registro = {}
                        registro['id']           = arquivo[x]['id'] 
                        registro['name']         = arquivo[x]['name']
                        registro['url']          = arquivo[x]['url']
                        registro['created_at']   = arquivo[x]['created_at']
                        registro['num_watchers'] = arquivo[x]['num_watchers']       
                        registro['releases']     = [] 
                        arquivo_saida.append(registro)
                    else:
                        if existe_releases: # Gera registro do repositorio com suas releases
                            registro = {}
                            registro['id']           = arquivo[x]['id'] 
                            registro['name']         = arquivo[x]['name']
                            registro['url']          = arquivo[x]['url']
                            registro['created_at']   = arquivo[x]['created_at']
                            registro['num_watchers'] = arquivo[x]['num_watchers']       
                            registro['releases']     = lista_releases
                            print(f'Quantidade de releases {len(lista_releases)}')
                            arquivo_saida.append(registro)     
                        
                    print("FIM repositório")
                    break
                else:

                    if i == 1: # Limpa a lista quando é a primeira chamada
                        lista_releases = []

                    existe_releases = True
                    # Pega todas as releases e insere na lista com o seu repositorio
                    for y in range(len(items)):       
                        lista_releases.append(items[y])
        
        if erro:
            break

    return arquivo_saida

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

#================================================================================#
# MAIN                                                                           #
#================================================================================#

print('Informe o arquivo.json dos repositórios: ')
nome_arquivo = input()

arquivo_json = ler_arquivo_json(nome_arquivo)

arquivo_json_saida = consulta_releases_repositorios(arquivo_json)

nome_arquivo_saida = f'releases-{str(nome_arquivo)}'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_saida)