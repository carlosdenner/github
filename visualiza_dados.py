import json
import sweetviz as sv
import pandas as pd    
import os

def arquivo_json_existe(file_name):
    return os.path.exists(file_name)

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

# Seleciona determinados campos do registro do arquivo de entrada
def seleciona_informacoes_repositorio_json(arquivo):
    lista = []

    for x in range(len(arquivo)):
        registro = {}
        registro['id']         = arquivo[x]['id']
        registro['forks']      = arquivo[x]['forks']
        registro['language']   = arquivo[x]['language']
        registro['created_at'] = arquivo[x]['created_at']
        lista.append(registro)
    
    return lista

#================================================================================#
# MAIN                                                                           #
#================================================================================#
nome_base_dados = "base_dados_repositorios.json"


if arquivo_json_existe(nome_base_dados):
    base_dados_json = ler_arquivo_json(nome_base_dados)
    base_dados = base_dados_json['items']

    lista = seleciona_informacoes_repositorio_json(base_dados)

    # Transforma o arquivo json em um data frame
    data_frame = pd.json_normalize(lista)

    analise_dados = sv.analyze(data_frame)

    analise_dados.show_html('analise_dados.html')
else:
    print(f'Erro - Arquivo {str(nome_base_dados)} não foi localizados!')
