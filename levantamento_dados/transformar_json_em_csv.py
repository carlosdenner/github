import json
import csv

# Leitura de arquivo json comum
def ler_arquivo_json_tipo_1(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

# Leitura de arquivo json linha a linha
def ler_arquivo_json_tipo_2(nome_arquivo):
    lista_json = []
    for line in open(nome_arquivo, 'r', encoding='utf8'):
        lista_json.append(json.loads(line))
    
    return lista_json

def grava_arquivo_csv(nome_arquivo,arquivo):
    with open(nome_arquivo, 'w') as outf:
        dw = csv.DictWriter(outf, arquivo[0].keys())
        dw.writeheader()
        for row in arquivo:
            dw.writerow(row)

print("Informe o arquivo.json que deseja transformar em .csv: ")
nome_arquivo = input()

print("Leitura de arquivo.json tipo 1 ou 2: ")
tipo_leitura = input()

if tipo_leitura == '1':
    print('Leitura tipo 1')
    arquivo_json = ler_arquivo_json_tipo_1(nome_arquivo)
else:
    print('Leitura tipo 2')
    arquivo_json = ler_arquivo_json_tipo_2(nome_arquivo)

print(f'Quantidade dos registros de entrada {len(arquivo_json)}')

print(f'Chaves do arquivo: {str(arquivo_json[0].keys())} ')

nome_arquivo_saida = f'{str(nome_arquivo)}.csv'

grava_arquivo_csv(nome_arquivo_saida, arquivo_json)