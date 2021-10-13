import requests
import json
import time
import datetime
from dateutil import parser

def requisicao_api(url,headers):
    resposta = requests.get(url,headers=headers)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return resposta.status_code

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def consulta_data_das_tags_repositorios(arquivo):
    arquivo_saida = []
    datafimghtorrent = datetime.datetime(year=2019,month=5,day=31)
    #
    for x in (range(200,250)):

        print(f'Repositório: {str(x)}')
        print(arquivo[x]['id'])

        lista_tags = arquivo[x]['tags']
        
        print(f'Tamanho da lista de tags: {str(len(lista_tags))}')

        if len(lista_tags) == 0:
            print('Repositório vazio')
            registro = {}
            registro['id']           = arquivo[x]['id'] 
            registro['name']         = arquivo[x]['name']
            registro['url']          = arquivo[x]['url']
            registro['created_at']   = arquivo[x]['created_at']
            registro['num_watchers'] = arquivo[x]['num_watchers']   
            registro['data']         = ""
            arquivo_saida.append(registro)  
        else:
            todos_fora_margem = True
            for i in range(len(lista_tags)):
                commit = lista_tags[i]['commit']
                url    = commit['url']

                headers = {
                    'Authorization' : 'token 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',
                    'Accept': 'application/vnd.github.mercy-preview+json', 
                    'Accept-Charset': 'UTF-8'
                }

                item = requisicao_api(url,headers)    

                if type(item) is int: # Caso ocorra algum erro, finaliza busca
                    print("Erro: " + str(item))
                    erro = True
                    break
                else:

                    if len(item) == 0: #Verifica se não existe registro que detalha a tag
                        print("ERRO - Não possui registro")
                        break
                    else:
                        # Transforma data do commit da tag e compara com data de criação do repositório e 31-05-2019
                        # Retira offset data - Acredito que seja informação de timezone
                        commit_tag      = item['commit']['committer']
                        data_commit_tag = parser.parse(commit_tag['date']).replace(tzinfo=None)

                        # Transforma data de criação do repositório em data normal
                        data_criacao = parser.parse(arquivo[x]['created_at']).replace(tzinfo=None)

                        # Pega o nome da versão da tag
                        versao          = lista_tags[i]['name']

                        # Grava somente registros que estão entre a data de criação e 31-05-2019
                        if data_commit_tag >= data_criacao and data_commit_tag <= datafimghtorrent:
                            registro = {}
                            registro['id']           = arquivo[x]['id'] 
                            registro['name']         = arquivo[x]['name']
                            registro['url']          = arquivo[x]['url']
                            registro['created_at']   = arquivo[x]['created_at']
                            registro['num_watchers'] = arquivo[x]['num_watchers']   
                            registro['versao']       = versao
                            data_formatada           = datetime.datetime.strftime(data_commit_tag, "%d-%m-%Y")
                            registro['data']         = data_formatada
                            arquivo_saida.append(registro)
                            todos_fora_margem        = False

            if todos_fora_margem:
                registro = {}
                registro['id']           = arquivo[x]['id'] 
                registro['name']         = arquivo[x]['name']
                registro['url']          = arquivo[x]['url']
                registro['created_at']   = arquivo[x]['created_at']
                registro['num_watchers'] = arquivo[x]['num_watchers']   
                registro['data']         = ""
                arquivo_saida.append(registro)

        
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

arquivo_json_saida = consulta_data_das_tags_repositorios(arquivo_json)

nome_arquivo_saida = f'tags-data-{str(nome_arquivo)}'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_saida)