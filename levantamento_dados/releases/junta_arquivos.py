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

print('Informe o arquivo.json 1: ')
nome_arquivo = input()

arquivo_json1 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 2: ')
nome_arquivo = input()

arquivo_json2 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 3: ')
nome_arquivo = input()

arquivo_json3 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 4: ')
nome_arquivo = input()

arquivo_json4 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 5: ')
nome_arquivo = input()

arquivo_json5 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 6: ')
nome_arquivo = input()

arquivo_json6 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 7: ')
nome_arquivo = input()

arquivo_json7 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 8: ')
nome_arquivo = input()

arquivo_json8 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 9: ')
nome_arquivo = input()

arquivo_json9 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 10: ')
nome_arquivo = input()

arquivo_json10 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 11: ')
nome_arquivo = input()

arquivo_json11 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 12: ')
nome_arquivo = input()

arquivo_json12 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 13: ')
nome_arquivo = input()

arquivo_json13 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 14: ')
nome_arquivo = input()

arquivo_json14 = ler_arquivo_json(nome_arquivo)

arquivo_resultado = arquivo_json1 + arquivo_json2  + arquivo_json3 + arquivo_json4 + arquivo_json5 + arquivo_json6 + arquivo_json7 + arquivo_json8 + arquivo_json9 + arquivo_json10 + arquivo_json11 + arquivo_json12 + arquivo_json13 + arquivo_json14

nome_arquivo_saida = 'arquivo-saida-junto.json'

gravar_arquivo_json(nome_arquivo_saida,arquivo_resultado)