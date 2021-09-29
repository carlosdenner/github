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

print('Informe o arquivo.json de code frequency: ')
nome_arquivo = input()

print('Informe o arquivo.json de repositorios: ')
nome_arquivo_repositorios = input()

arquivo_json = ler_arquivo_json(nome_arquivo)

arquivo_json_repo = ler_arquivo_json(nome_arquivo_repositorios)

repo_id_ant = 0
qtd = 0

lista_de_repositorios = []

for i in range(len(arquivo_json)):
    
    if repo_id_ant != arquivo_json[i]['id']:

        repo_id_ant = arquivo_json[i]['id']
        qtd = qtd + 1

        registro = {}
        registro ['repo_id'] = repo_id_ant

        lista_de_repositorios.append(registro)

print(len(lista_de_repositorios))

for i in range(len(arquivo_json_repo)):

        achou = False

        for x in range(len(lista_de_repositorios)):
            if str(arquivo_json_repo[i]['id']) == lista_de_repositorios[x]['repo_id']:
                achou = True

        if achou == False:
            repositorio = str(arquivo_json_repo[i]['id'])
            nome = str(arquivo_json_repo[i]['name'])
            print(f'Repositorio {repositorio} não encontrado')
            print(f'Nome {nome}')

print(f'Quantidade de registros: {str(len(arquivo_json))}')
print(f'Quantidade de repositórios no arquivo: {str(qtd)}')
