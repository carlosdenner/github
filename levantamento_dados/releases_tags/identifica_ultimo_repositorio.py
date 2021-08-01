import json

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

#================================================================================#
# MAIN                                                                           #
#================================================================================#

print('Informe o arquivo.json dos repositórios: ')
nome_arquivo = input()

arquivo_json = ler_arquivo_json(nome_arquivo)

print(arquivo_json[len(arquivo_json)-1]['id'])
print(arquivo_json[len(arquivo_json)-1]['name'])
print(len(arquivo_json))
