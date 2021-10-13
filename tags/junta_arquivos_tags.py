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
arquivo_1 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 2: ')
nome_arquivo = input()
arquivo_2 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 3: ')
nome_arquivo = input()
arquivo_3 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 4: ')
nome_arquivo = input()
arquivo_4 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 5: ')
nome_arquivo = input()
arquivo_5 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 6: ')
nome_arquivo = input()
arquivo_6 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 7: ')
nome_arquivo = input()
arquivo_7 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 8: ')
nome_arquivo = input()
arquivo_8 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 9: ')
nome_arquivo = input()
arquivo_9 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 10: ')
nome_arquivo = input()
arquivo_10 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 11: ')
nome_arquivo = input()
arquivo_11 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 12: ')
nome_arquivo = input()
arquivo_12 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 13_1: ')
nome_arquivo = input()
arquivo_13_1 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 13_2: ')
nome_arquivo = input()
arquivo_13_2 = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 14: ')
nome_arquivo = input()
arquivo_14   = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 15: ')
nome_arquivo = input()
arquivo_15   = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 16: ')
nome_arquivo = input()
arquivo_16   = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 17: ')
nome_arquivo = input()
arquivo_17   = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 18: ')
nome_arquivo = input()
arquivo_18   = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 19: ')
nome_arquivo = input()
arquivo_19   = ler_arquivo_json(nome_arquivo)

print('Informe o arquivo.json 20: ')
nome_arquivo = input()
arquivo_20   = ler_arquivo_json(nome_arquivo)

arquivo_saida = []

for i in range(len(arquivo_1)):
    arquivo_saida.append(arquivo_1[i])

for i in range(len(arquivo_2)):
    arquivo_saida.append(arquivo_2[i])

for i in range(len(arquivo_3)):
    arquivo_saida.append(arquivo_3[i])

for i in range(len(arquivo_4)):
    arquivo_saida.append(arquivo_4[i])

for i in range(len(arquivo_5)):
    arquivo_saida.append(arquivo_5[i])

for i in range(len(arquivo_6)):
    arquivo_saida.append(arquivo_6[i])

for i in range(len(arquivo_7)):
    arquivo_saida.append(arquivo_7[i])

for i in range(len(arquivo_8)):
    arquivo_saida.append(arquivo_8[i])

for i in range(len(arquivo_9)):
    arquivo_saida.append(arquivo_9[i])

for i in range(len(arquivo_10)):
    arquivo_saida.append(arquivo_10[i])

for i in range(len(arquivo_11)):
    arquivo_saida.append(arquivo_11[i])

for i in range(len(arquivo_12)):
    arquivo_saida.append(arquivo_12[i])

for i in range(len(arquivo_13_1)):
    arquivo_saida.append(arquivo_13_1[i])

for i in range(len(arquivo_13_2)):
    arquivo_saida.append(arquivo_13_2[i])

for i in range(len(arquivo_14)):
    arquivo_saida.append(arquivo_14[i])

for i in range(len(arquivo_15)):
    arquivo_saida.append(arquivo_15[i])

for i in range(len(arquivo_16)):
    arquivo_saida.append(arquivo_16[i])

for i in range(len(arquivo_17)):
    arquivo_saida.append(arquivo_17[i])

for i in range(len(arquivo_18)):
    arquivo_saida.append(arquivo_18[i])

for i in range(len(arquivo_19)):
    arquivo_saida.append(arquivo_19[i])

for i in range(len(arquivo_20)):
    arquivo_saida.append(arquivo_20[i])

nome_arquivo_saida = f'saida-{nome_arquivo}'

gravar_arquivo_json(nome_arquivo_saida,arquivo_saida)