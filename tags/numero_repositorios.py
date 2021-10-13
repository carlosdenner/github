import json

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)


#================================================================================#
# MAIN                                                                           #
#================================================================================#

print('Informe o arquivo.json das tags: ')
nome_arquivo_tags = input()

arquivo_json = ler_arquivo_json(nome_arquivo_tags)

repo_id_ant = 0

qtd = 0

for i in range(len(arquivo_json)):  
    if arquivo_json[i]['id'] != repo_id_ant:
        repo_id_ant = arquivo_json[i]['id']
        qtd = qtd + 1

print(f'Quantidade: {str(qtd)}')
