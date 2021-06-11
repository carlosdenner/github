import json
import sweetviz as sv
import pandas as pd    

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

base_dados_json = ler_arquivo_json(nome_base_dados)
base_dados = base_dados_json['items']

lista = seleciona_informacoes_repositorio_json(base_dados)

# Transforma o arquivo json em um data frame
data_frame = pd.json_normalize(lista)

analise_dados = sv.analyze(data_frame)

analise_dados.show_html('analise_dados.html')