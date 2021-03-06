import json
import os

def arquivo_json_existe(file_name):
    return os.path.exists(file_name)

def busca_registro_no_arquivo(arquivo,registro):
    for x in range(len(arquivo)):
        if registro['id'] == arquivo[x]['id']:
            return x
    
    return False

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

def inclui_arquivo_na_base_dados(arquivo):
    global nome_base_dados 
    arquivo_json = {}

    if arquivo_json_existe(nome_base_dados): # Verifica se base de dados já existe
        base_dados_json = ler_arquivo_json(nome_base_dados)

        base_dados = base_dados_json['items']

        # Percorre arquivo que sera incluido na base de dados
        # Caso registro exista     -> Atualiza
        # Caso registro não exista -> Inclui no final
        for x in range(len(arquivo)):
            resultado = busca_registro_no_arquivo(base_dados,arquivo[x])
            if type(resultado) is int:
                base_dados[resultado] = arquivo[x]
            else:
                base_dados.append(arquivo[x]) 
        
        arquivo_json['items'] = base_dados
    else:
        arquivo_json['items'] = arquivo
        
    gravar_arquivo_json(nome_base_dados,arquivo_json)
    
    return 0
        
#================================================================================#
# MAIN                                                                           #
#================================================================================#
nome_base_dados = "base_dados_repositorios.json"

print("Informe o nome do arquivo.json que deseja incluir na base de dados: ")
nome_arquivo = input()

if arquivo_json_existe(nome_arquivo):
    arquivo = ler_arquivo_json(nome_arquivo)
    inclui_arquivo_na_base_dados(arquivo['items'])
else:
    print(f'Erro - Arquivo {str(nome_arquivo)} não foi localizados!')
