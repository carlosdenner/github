import json
import datetime
from dateutil import parser

def processar_arquivo_entrada(arquivo):
    arquivo_saida = []
    datainicio          = datetime.datetime(year=1970,month=1,day=1,hour=0,minute=0,second=0,microsecond=0)
    datafimghtorrent    = datetime.datetime(year=2019,month=5,day=31)
    datainicioghtorrent = datetime.datetime(year=2012,month=2,day=1)

    for i in range(len(arquivo)):
        repo_id              = arquivo[i]['id']
        data_hora            = parser.parse(arquivo[i]['created_at'])
        created_at           = datetime.datetime.strftime(data_hora, "%d-%m-%Y")

        if len(arquivo[i]['code_frequency']) > 0 and repo_id != "75608247" and repo_id != "51958423":
        
            lista_code_frequency = arquivo[i]['code_frequency']
                
            for x in (range(len(lista_code_frequency))):
                registro                       = {}
                registro['repo_id']            = repo_id
                registro['data_criacao']       = created_at
                segundos                       = lista_code_frequency[x][0]
                
                # Transforma segundos em dias
                days = segundos // 86400
                data_hora_registro = datainicio + datetime.timedelta(days=int(days))

                # Somente seleciona os registros que estão entre 01-02-2012 31-05-2019 - Período da base do GHTorrent
                if data_hora_registro >= datainicioghtorrent and data_hora_registro <= datafimghtorrent:
                    # Transforma timestamp em data
                    data = datetime.datetime.strftime(data_hora_registro , "%d-%m-%Y")
           
                    registro['data']               = data 
                    # Linhas alteradas é igual a soma absoluta de linhas adicionadas e deletadas
                    registro['linhas_alteradas']   = int(lista_code_frequency[x][1]) + ( int(lista_code_frequency[x][2]) * -1)
                
                    arquivo_saida.append(registro)

        else: 
            registro                       = {}
            registro['repo_id']            = repo_id
            registro['data_criacao']       = created_at
            registro['data']               = created_at
            registro['linhas_alteradas']   = 0
            arquivo_saida.append(registro)

    return arquivo_saida

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

arquivo_json = ler_arquivo_json(nome_arquivo)

arquivo_json_saida = processar_arquivo_entrada(arquivo_json)

nome_arquivo_saida = f'saida-{str(nome_arquivo)}'

print(f'Quantidade de registros de saida: {str(len(arquivo_json_saida))}')

gravar_arquivo_json(nome_arquivo_saida, arquivo_json_saida)