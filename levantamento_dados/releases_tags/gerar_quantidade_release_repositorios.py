import json

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

#================================================================================#
# MAIN                                                                           #
#================================================================================#

print('Informe o arquivo.json dos repositórios com suas releases: ')
nome_arquivo = input()

arquivo_json = ler_arquivo_json(nome_arquivo)

arquivo_json_saida = []

for x in range(len(arquivo_json)):
    registro = {}
    registro['id']                  = arquivo_json[x]['id'] 
    registro['name']                = arquivo_json[x]['name']
    registro['url']                 = arquivo_json[x]['url']
    registro['created_at']          = arquivo_json[x]['created_at']
    registro['num_watchers']        = arquivo_json[x]['num_watchers']   
    registro['quantidade_releases'] = len(arquivo_json[x]['releases'])
    arquivo_json_saida.append(registro)

nome_arquivo_saida = f'quantidade-releases-repositorio.json'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_saida)