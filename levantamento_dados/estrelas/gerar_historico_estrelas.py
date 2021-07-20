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

def gerar_historico_estrelas(arquivo_json):
    arquivo_saida = []
    repo_id_ant = 0
    qtd_estrelas_ant = 0
    repo_ant = {}

    for i in range(len(arquivo_json)):
        
        if arquivo_json[i]['repo_id'] != repo_id_ant:
            
            if repo_id_ant != 0:
                qtd_dias = diferenca_entre_datas(repo_ant['data'],'31-05-2019')

                data = datetime.datetime.strptime(repo_ant['data'], "%d-%m-%Y")
                
                for x in range(qtd_dias):
                    data = data + timedelta(days=1)
                    data_string = datetime.datetime.strftime(data,"%d-%m-%Y")
                    registro = {}
                    registro['id']       = repo_ant['repo_id']
                    registro['data']     = data_string
                    registro['estrelas'] = qtd_estrelas_ant
                    arquivo_saida.append(registro)


            repo_id_ant = arquivo_json[i]['repo_id'] 
            qtd_estrelas_ant = 0

            if arquivo_json[i]['data_criacao'] != arquivo_json[i]['data']:
                
                qtd_dias = diferenca_entre_datas(arquivo_json[i]['data_criacao'],arquivo_json[i]['data'])
            
                data_estrelas = datetime.datetime.strptime(arquivo_json[i]['data'],"%d-%m-%Y")
                data_criacao = datetime.datetime.strptime(arquivo_json[i]['data_criacao'],"%d-%m-%Y")

                if data_criacao < data_estrelas:
                    data = data_criacao
                    for x in range(qtd_dias+1):
                        data_string = datetime.datetime.strftime(data,"%d-%m-%Y")
                        registro = {}
                        registro['id']       = arquivo_json[i]['repo_id']
                        registro['data']     = data_string
                        if arquivo_json[i]['data'] == data_string:
                            registro['estrelas'] = int(arquivo_json[i]['quantidade_estrelas'])
                            qtd_estrelas_ant     = int(arquivo_json[i]['quantidade_estrelas'])
                        else:
                            registro['estrelas'] = 0
                        arquivo_saida.append(registro)
                        data = data + timedelta(days=1)
                else:
                    data = data_estrelas
                    data_string = datetime.datetime.strftime(data,"%d-%m-%Y")
                    registro = {}
                    registro['id']       = arquivo_json[i]['repo_id']
                    registro['data']     = data_string
                    registro['estrelas'] = int(arquivo_json[i]['quantidade_estrelas'])
                    qtd_estrelas_ant     = int(arquivo_json[i]['quantidade_estrelas'])
                    arquivo_saida.append(registro)
                    
            else:
                registro = {}
                registro['id']       = arquivo_json[i]['repo_id']
                registro['data']     = arquivo_json[i]['data_criacao']
                registro['estrelas'] = int(arquivo_json[i]['quantidade_estrelas'])
                qtd_estrelas_ant     = int(arquivo_json[i]['quantidade_estrelas'])
                arquivo_saida.append(registro)   
        else:
            
            qtd_dias = diferenca_entre_datas(repo_ant['data'],arquivo_json[i]['data'])

            data = datetime.datetime.strptime(repo_ant['data'], "%d-%m-%Y")

            for y in range(qtd_dias):
                data = data + timedelta(days=1)
                data_string = datetime.datetime.strftime(data,"%d-%m-%Y")
                registro = {}
                registro['id']       = arquivo_json[i]['repo_id']
                registro['data']     = data_string
                if arquivo_json[i]['data'] == data_string:
                    qtd_estrelas_ant = qtd_estrelas_ant + int(arquivo_json[i]['quantidade_estrelas']) 
                registro['estrelas'] = qtd_estrelas_ant
                arquivo_saida.append(registro)     

             
        repo_ant = arquivo_json[i]
  
    return arquivo_saida

def gravar_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=False, separators=(',' , ':'))



print("Informe o nome do arquivo.json das estrelas: ")
nome_arquivo_estrelas = input()

arquivo_json = ler_arquivo_json_tipo_1(nome_arquivo_estrelas)

arquivos_json_saida = gerar_historico_estrelas(arquivo_json)

nome_arquivo_estrelas_saida = f'saida-{str(nome_arquivo_estrelas)}'

gravar_arquivo_json(nome_arquivo_estrelas_saida,arquivos_json_saida)
