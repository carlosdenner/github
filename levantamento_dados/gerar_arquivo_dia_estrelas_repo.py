import json
import datetime
import operator
from datetime import timedelta
from dateutil import parser

def diferenca_entre_datas(data1, data2):
    d1 = datetime.datetime.strptime(data1, "%d-%m-%Y")
    d2 = datetime.datetime.strptime(data2, "%d-%m-%Y")
    return abs((d1 - d2).days)

def ler_arquivo_json_tipo_1(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

# Leitura de arquivo json linha a linha
def ler_arquivo_json_tipo_2(nome_arquivo):
    lista_json = []
    for line in open(nome_arquivo, 'r', encoding='utf8'):
        lista_json.append(json.loads(line))
    
    return lista_json

# Gerar lista de repositorios desde sua data de criacao até uma data limite com estrelas zeradas
def gerar_datas_repositorios_criacao_ate_fim(arquivo_json):
    arquivo_saida = []

    for i in range(len(arquivo_json)):
        
        # Formata a data de criação do repositório
        data_criacao_utc = arquivo_json[i]['created_at']
        data_criacao = parser.parse(data_criacao_utc)
        data_criacao = datetime.datetime.strftime(data_criacao, "%d-%m-%Y")
        
        # Calcula a diferença entre a data de criação e a data limite
        qtd_dias = diferenca_entre_datas(data_criacao,'12-07-2021')
        
        data_hora = parser.parse(data_criacao)
        
        # Cria registro para todas as datas entre a data de criação
        # e a data limite informando número de estrelas zerado
        for x in range(qtd_dias):
            data_hora = data_hora + timedelta(days=1)
            data = datetime.datetime.strftime(data_hora, "%d-%m-%Y")
            registro = {}
            registro['id']       = arquivo_json[i]['id']
            registro['data']     = data
            registro['estrelas'] = 0
            arquivo_saida.append(registro)
            
    return arquivo_saida

def calcular_estrelas_cada_dia(arquivo,arquivo_estrelas):
    repo_ant_id = 0
    estrelas_ant = 0

    for i in range(len(arquivo)):

        # Quando chega repositório novo zera o repositório anterior
        if arquivo[i]['id'] != repo_ant_id:
            print(arquivo[i]['id'])
            estrelas_ant = 0
            repo_ant_id = arquivo[i]['id']

        print(arquivo[i]['data'])

        # Filtra as estrelas do repositorio naquele dia
        # Forma uma lista e conta quantos registros tem na lista 
        quantidade = len(list(filter(lambda x:x["repo_id"]    == arquivo[i]['id'] and 
                                              x["created_at"] == arquivo[i]['data'],
                                              arquivo_estrelas)))

        estrelas_ant = estrelas_ant + quantidade
        arquivo[i]['estrelas'] = estrelas_ant
        
    return arquivo

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))

#================================================================================#
# MAIN                                                                           #
#================================================================================#

print("Informe o arquivo.json dos repositórios: ")
nome_arquivo_repositorios = input()

print("Informe o nome do arquivo.json das estrelas: ")
nome_arquivo_estrelas = input()

arquivo_json_repositorios_1 = ler_arquivo_json_tipo_1(nome_arquivo_repositorios)

arquivo_json_repositorios = []

# arquivo_json_repositorios_1.sort(key=operator.itemgetter('id'), reverse=True)

for x in range(1):
    arquivo_json_repositorios.append(arquivo_json_repositorios_1[x])

print(arquivo_json_repositorios[0])

arquivo_json_repositorios.sort(key=operator.itemgetter('id'), reverse=True)

arquivo_json_saida_repo = gerar_datas_repositorios_criacao_ate_fim(arquivo_json_repositorios)

arquivo_json_estrelas = ler_arquivo_json_tipo_1(nome_arquivo_estrelas)

arquivo_json_estrelas.sort(key=operator.itemgetter('repo_id'), reverse=True)

arquivo_saida = calcular_estrelas_cada_dia(arquivo_json_saida_repo,arquivo_json_estrelas)

gravar_arquivo_json("saida2.json",arquivo_saida)