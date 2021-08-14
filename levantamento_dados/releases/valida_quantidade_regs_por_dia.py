import json

def ler_arquivo_json_tipo_1(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

print("Informe o nome do arquivo.json: ")
nome_arquivo = input()

arquivo_json = ler_arquivo_json_tipo_1(nome_arquivo)

arquivo_json_saida = []

for x in range(len(arquivo_json)):
    if arquivo_json[x]['data'] == '31-05-2019':
        arquivo_json_saida.append(arquivo_json[x])


nome_arquivo_saida = f'saida-valida-{str(nome_arquivo)}'

gravar_arquivo_json(nome_arquivo_saida,arquivo_json_saida)