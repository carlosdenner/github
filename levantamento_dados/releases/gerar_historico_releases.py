import json
import datetime
from datetime import timedelta
from dateutil import parser

def diferenca_entre_datas(data1, data2):
    d1 = datetime.datetime.strptime(data1, "%d-%m-%Y")
    d2 = datetime.datetime.strptime(data2, "%d-%m-%Y")
    return abs((d1 - d2).days)

def ler_arquivo_json_tipo_1(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def gerar_historico_releases(arquivo_json):
    arquivo_saida = []
    repo_id_ant = 0
    qtd_releases_ant = 0
    repo_ant = {}

    for i in range(len(arquivo_json)):
        
        print(arquivo_json[i]['name'])

        if arquivo_json[i]['data'] == "":
            arquivo_json[i]['data'] = arquivo_json[i]['data_criacao']

        if arquivo_json[i]['id'] != repo_id_ant:

            if repo_id_ant != 0 and repo_ant['data'] != "":
                qtd_dias = diferenca_entre_datas(repo_ant['data'],'31-05-2019')

                data = datetime.datetime.strptime(repo_ant['data'], "%d-%m-%Y")
                    
                for x in range(qtd_dias):
                    data = data + timedelta(days=1)
                    data_string = datetime.datetime.strftime(data,"%d-%m-%Y")
                    registro = {}
                    registro['id']       = repo_ant['id']
                    registro['data']     = data_string
                    registro['releases']    = qtd_releases_ant
                    arquivo_saida.append(registro)


            repo_id_ant = arquivo_json[i]['id'] 
            qtd_releases_ant = 0

            if arquivo_json[i]['data_criacao'] != arquivo_json[i]['data']:
                    
                qtd_dias = diferenca_entre_datas(arquivo_json[i]['data_criacao'],arquivo_json[i]['data'])
                
                data_releases = datetime.datetime.strptime(arquivo_json[i]['data'],"%d-%m-%Y")
                data_criacao = datetime.datetime.strptime(arquivo_json[i]['data_criacao'],"%d-%m-%Y")

                if data_criacao < data_releases:
                    data = data_criacao
                    for x in range(qtd_dias+1):
                        data_string = datetime.datetime.strftime(data,"%d-%m-%Y")
                        registro = {}
                        registro['id']       = arquivo_json[i]['id']
                        registro['data']     = data_string
                        if arquivo_json[i]['data'] == data_string:
                            registro['releases'] = int(arquivo_json[i]['quantidade_releases'])
                            qtd_releases_ant     = int(arquivo_json[i]['quantidade_releases'])
                        else:
                            registro['releases'] = 0
                        arquivo_saida.append(registro)
                        data = data + timedelta(days=1)
                else:
                    data = data_releases
                    data_string = datetime.datetime.strftime(data,"%d-%m-%Y")
                    registro = {}
                    registro['id']       = arquivo_json[i]['id']
                    registro['data']     = data_string
                    registro['releases']    = int(arquivo_json[i]['quantidade_releases'])
                    qtd_releases_ant        = int(arquivo_json[i]['quantidade_releases'])
                    arquivo_saida.append(registro)
                    
            else:
                registro = {}
                registro['id']       = arquivo_json[i]['id']
                registro['data']     = arquivo_json[i]['data_criacao']
                registro['releases']    = int(arquivo_json[i]['quantidade_releases'])
                qtd_releases_ant        = int(arquivo_json[i]['quantidade_releases'])
                arquivo_saida.append(registro)   
        else:
            
            qtd_dias = diferenca_entre_datas(repo_ant['data'],arquivo_json[i]['data'])

            data = datetime.datetime.strptime(repo_ant['data'], "%d-%m-%Y")

            for y in range(qtd_dias):
                data = data + timedelta(days=1)
                data_string = datetime.datetime.strftime(data,"%d-%m-%Y")
                registro = {}
                registro['id']       = arquivo_json[i]['id']
                registro['data']     = data_string
                if arquivo_json[i]['data'] == data_string:
                    qtd_releases_ant = qtd_releases_ant + int(arquivo_json[i]['quantidade_releases']) 
                registro['releases'] = qtd_releases_ant
                arquivo_saida.append(registro)     

             
        repo_ant = arquivo_json[i]
  
    return arquivo_saida

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))


#================================================================================#
# MAIN                                                                           #
#================================================================================#

print("Informe o nome do arquivo.json dos releases: ")
nome_arquivo_releases = input()

arquivo_json = ler_arquivo_json_tipo_1(nome_arquivo_releases)

arquivos_json_saida = gerar_historico_releases(arquivo_json)

nome_arquivo_releases_saida = f'saida-{str(nome_arquivo_releases)}'

gravar_arquivo_json(nome_arquivo_releases_saida,arquivos_json_saida)
