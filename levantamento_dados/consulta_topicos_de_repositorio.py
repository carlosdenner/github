import requests
import json
import os

def arquivo_json_existe(file_name):
    return os.path.exists(file_name)

def requisicao_api(url,headers):
    resposta = requests.get(url,headers=headers)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return resposta.status_code

# Leitura de arquivo json comum 
def ler_arquivo_json_tipo_1(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

# Leitura de arquivo json linha a linha
def ler_arquivo_json_tipo_2(nome_arquivo):
    lista_json = []
    for line in open(nome_arquivo, 'r', encoding='utf8'):
        lista_json.append(json.loads(line))

    return lista_json

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

# Pesquisa repositorios via requisicao na API
def consulta_repostorios(arquivo_json):
    
    qtd_req = 0

    arquivo_json_saida = []

    for i in range(0,10):
        qtd_req = qtd_req + 1
        
        print(arquivo_json[i]['url'])
            
        headers = {'Accept': 'application/vnd.github.mercy-preview+json', 'Accept-Charset': 'UTF-8'}

        dados_api = requisicao_api(arquivo_json[i]['url'],headers)    

        if type(dados_api) is int: # Caso ocorra algum erro, finaliza busca
            if dados_api == 403:
                print("ERRO 403 - Finaliza processo.")
                break
            else:
                if dados_api == 404 or dados_api == 451: # Registro não encontrado - Deixa sem tópicos
                    print(f"ERRO {str(dados_api)} - Repositório não encontrado.")
                    arquivo_json[i]['list_topics'] = [] # Deixa lista de tópicos em branco
                    arquivo_json_saida.append(arquivo_json[i])
                else:        
                    print("Erro: " + str(dados_api))
                    break
        else:
            print(dados_api['topics'])

            arquivo_json[i]['list_topics'] = dados_api['topics']

            arquivo_json_saida.append(arquivo_json[i])
                
    return arquivo_json_saida

# Verifica se o repositorio está na base de dados json. Em caso positivo, atribui a lista de topicos.
def consulta_topicos_base_de_dados_json(base_dados_json, arquivo_json):
    arquivo_json_topicos = []
    arquivo_json_nao_encontrado = []
    arquivo_json_nao_encontrado_2 = []
    global arquivo_json_busca_requisicao

    # Pesquisa por URL
    for i in range(len(arquivo_json)):
        achou = False
        for x in range(len(base_dados_json)):
            if arquivo_json[i]['url'] == base_dados_json[x]['url']:
                arquivo_json[i]['list_topics'] = base_dados_json[x]['topics']
                arquivo_json_topicos.append(arquivo_json[i])
                achou = True
                break

        if not achou: 
            #print(arquivo_json[i]['url'])
            arquivo_json_nao_encontrado.append(arquivo_json[i])

    # Pesquisa por Nome e Timestamp de criação
    for i in range(len(arquivo_json_nao_encontrado)):
        achou = False
        # Formata data de UTC para T Z
        data_hora = arquivo_json_nao_encontrado[i]['created_at'].replace(" UTC","Z")
        data_hora_formatada = data_hora.replace(" ","T")
        for x in range(len(base_dados_json)):
            if (arquivo_json_nao_encontrado[i]['name']       == base_dados_json[x]['name'] and
                data_hora_formatada                          == base_dados_json[x]['created_at']):
                arquivo_json_nao_encontrado[i]['list_topics'] = base_dados_json[x]['topics']
                arquivo_json_topicos.append(arquivo_json_nao_encontrado[i])
                achou = True
                break

        if not achou: 
            arquivo_json_nao_encontrado_2.append(arquivo_json_nao_encontrado[i])
    
    # Pesquisa por Timestamp de criação
    for i in range(len(arquivo_json_nao_encontrado_2)):
        achou = False
        # Formata data de UTC para T Z
        data_hora = arquivo_json_nao_encontrado_2[i]['created_at'].replace(" UTC","Z")
        data_hora_formatada = data_hora.replace(" ","T")
        for x in range(len(base_dados_json)):
            if (data_hora_formatada == base_dados_json[x]['created_at']):
                arquivo_json_nao_encontrado_2[i]['list_topics'] = base_dados_json[x]['topics']
                arquivo_json_topicos.append(arquivo_json_nao_encontrado_2[i])
                achou = True
                break

        if not achou: 
            print(arquivo_json_nao_encontrado_2[i]['name'])
            print(arquivo_json_nao_encontrado_2[i]['created_at'])

    return arquivo_json_topicos

def compara_arquivos_json(arquivo_json_1,arquivo_json_2):
    arquivo_json_saida = []

    for i in range(len(arquivo_json_1)):
        fim = False
        for x in range(len(arquivo_json_2)):
            if arquivo_json_1[i]['id'] == arquivo_json_2[x]['id']:
                fim = True
        
        if not fim: 
            arquivo_json_saida.append(arquivo_json_1[i])
    
    return arquivo_json_saida

#================================================================================#
# MAIN                                                                           #
#================================================================================#

nome_base_dados = "base_dados_repositorios.json"

print("Informe o nome do arquivo.json que deseja consultar os topicos na base de dados: ")
nome_arquivo = input()

if arquivo_json_existe(nome_arquivo):
    
    print("Deseja pesquisar quantos registros do arquivo informado: ")
    quantidade_registros_pesquisa = input()

    print("Deseja pesquisa no banco de dados? ")
    resposta = input()

    arquivo_json = ler_arquivo_json_tipo_2(nome_arquivo)
    base_dados = ler_arquivo_json_tipo_1(nome_base_dados)
    base_dados_json = base_dados['items']

    # Seleciona os x registros 
    arquivo_json_reg_selecao = []

    for i in range(int(quantidade_registros_pesquisa)):
        arquivo_json_reg_selecao.append(arquivo_json[i])
    
    nome_arquivo_saida = f'resultado-{str(nome_arquivo)}'
    
    if resposta == 'S': # Pesquisa na base somente na primeira requisição
        arquivo_json_topicos = consulta_topicos_base_de_dados_json(base_dados_json, arquivo_json_reg_selecao)

        print(f'Quantidade de registros encontrados: {str(len(arquivo_json_topicos))}')

        gravar_arquivo_json(nome_arquivo_saida, arquivo_json_topicos)

    # Ler o arquivo de saida para verificar quantos registros precisam ser pesquisados na requisição
    arquivo_json_total = ler_arquivo_json_tipo_1(nome_arquivo_saida)

    print(f'Quantidade de registros lidos da saida: {str(len(arquivo_json_total))}')
    
    # Seleciona somente os registros que precisam ser pesquisados via requisição
    arquivo_json_restante_req = compara_arquivos_json(arquivo_json_reg_selecao,arquivo_json_total)

    # Realiza as requisições
    arquivo_json_result_req = consulta_repostorios(arquivo_json_restante_req)

    print(f'Quantidade de registros encontrados nas requisições: {str(len(arquivo_json_result_req))}')
    
    # Pega os arquivos da requisição e coloca junto os que já existem no arquivo de saida
    for i in range(len(arquivo_json_result_req)):
        arquivo_json_total.append(arquivo_json_result_req[i])

    print(f'Quantidade de registros total: {str(len(arquivo_json_total))}')

    gravar_arquivo_json(nome_arquivo_saida, arquivo_json_total)
else:
    print(f'Erro - Arquivo {str(nome_arquivo)} não foi localizados!')