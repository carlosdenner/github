# LEVANTAMENTO DE DADOS GITHUB

## Processos para acessar dados do Github utilizando a API de REST do GitHub e base de dados do ghTorrent (BigQuery). Esses dados servirão como base para realizar análises de fins acadêmicos.

### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas: 
[Git](https://git-scm.com), [Python3](https://www.python.org/). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)
Também é utilizada a biblioteca [Sweetviz](https://pypi.org/project/sweetviz/).

```bash

# Instalação Git
$ sudo apt-get install git

# Instalação Python3 
$ sudo apt-get install python3

# Instalação do Pip
$ sudo apt install python3-pip

# Instalação da biblioteca Sweetviz
$ pip install sweetviz

# Clone este repositório
$ git clone <https://github.com/carlosdenner/github.git>

# Acesse a pasta levantamento_dados
$ cd levantamento_dados

```

### Módulos

#### Módulos para acessar repositórios do Github:

- **consulta_repositorios.py**: recebe como entrada as palavras-chave que deseja pesquisa e seus respectivos valores. Exemplo: Deseja pesquisa repositórios com o tópico open-data, então deve ser informado palavra-chave = topic e valor palavra-chave = open-data. Sua saída é um arquivo JSON com o seguinte formato: palavras-chave:valor palavra-chave-timestamp.json (topic:open-data-2021-06-12 21:21:29.719105.json).
- **consulta_repositorios_todos.py**: versão mais robusta do consulta_repositorios.py. O script busca mais de 1000 repositórios utilizando a ordenação do número de estrelas de cada repositório. Recomendado utilizar para pesquisas maiores, como exemplo: pesquisar os repositórios da linguagem Python - language:python.
- **consulta_topicos_de_repositorio.py**: recebe como entrada o arquivo.json com os repositórios que deseja pesquisar os tópicos. Primeiro ele pesquisa na base de dados de repositórios com as seguintes chaves e na seguinte ordem: a) url -> b) name e data de criação -> c) data de criação. Para os casos não encontrados na base de dados são feitas requisições na API do GITHUB. Essas requisições podem ter problema de erro 403, por isso, são acionadas no último caso, o mais recomendado é alimentar a base de dados com os dados desejados utilizando os scripts de consulta acioma e o script de atualização abaixo.
- **atualiza_base.py**: atualiza o arquivo JSON central chamado base_dados_repositorios.json. Recebe como entrada um arquivo contruido no consulta_repositorio.py e verifica repositório a repositório. Caso o repositório exista na base de dados faz atualização, caso não exista inclui na base de dados.
- **visualiza_dados.py**: recebe como entrada o arquivo central base de dados e faz análises com suas informações. Gera como saída gráficos em um arquivo html chamado analise_dados.html.

### Módulos para manipular arquivos JSON com informações de estrelas:
Na pasta **estrelas**:

- **identifica_data_criacao_repositorio.py**: recebe como entrada arquivo de repositórios e arquivo de histórico de estrelas. Identifica a data de criação do repositório e inclui no registro mais antigo do histórico de estrelas e retorna esse arquivo.
- **gerar_historico_estrelas.py**: recebe como entrada arquivo com o histórico de estrelas somado por data e também com a data de criação do repositório. Retorna o arquivo com o histórico da quantidade de estrelas que o repositório possui em cada dia desde sua criação até 31/05/2019 (ùltima atualização da base de dados do BigQuery).
- **gerar_arquivo_dia_estrelas_repo.py**: recebe como entrada arquivo com o histórico de estrelas original e arquivo com os repositórios. Retorna as mesmas informações do módulo acima, porém, não possui performace suficiente para processar muitos registros.

### Módulos para manipular arquivos JSON com informações de forks:
Na pasta **forks**:

- **identifica_data_criacao_repositorio.py**: recebe como entrada arquivo de repositórios e arquivo de histórico de forks. Identifica a data de criação do repositório e inclui no registro mais antigo do histórico de forks e retorna esse arquivo.
- **gerar_historico_forks.py**: recebe como entrada arquivo com o histórico de forks somado por data e também com a data de criação do repositório. Retorna o arquivo com o histórico da quantidade de forks que o repositório possui em cada dia desde sua criação até 31/05/2019 (ùltima atualização da base de dados do BigQuery).

### Módulos para manipular arquivos JSON com informações de contribuidores:
O **contribuidor** é um usuário que fez um commit no projeto. O data do primeiro commit é considerada a data de ingresso do contribuidor no projeto.
Na pasta **contribuidores**:

- **identifica_data_criacao_repositorio.py**: recebe como entrada arquivo de repositórios e arquivo de histórico de contribuidores. Identifica a data de criação do repositório e inclui no registro mais antigo do histórico de contribuidores e retorna esse arquivo.
- **gerar_historico_contribuidores.py**: recebe como entrada arquivo com o histórico de contribuidores somado por data e também com a data de criação do repositório. Retorna o arquivo com o histórico da quantidade de contribuidores que o repositório possui em cada dia desde sua criação até 31/05/2019 (ùltima atualização da base de dados do BigQuery).

### Módulos auxiliares para formatação:

- **transformar_created_at_em_data.py**: transformar a data created_at formato timestamp UTC em data formato dd-mm-yyyy.
- **transformar_json_em_csv**: converte um arquivo.json em .csv.

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python3](https://www.python.org/)
- [JSON](https://www.json.org/json-en.html)

### Dados

Os dados gerados nesse projeto podem ser acessados pelo link abaixo:
- [Dados](https://drive.google.com/drive/folders/1nwXFGrAOknPYeDqSTQfKhwJRTe4GvilS?usp=sharing)

#### Criação de banco de dados

##### Histórico de quantidade de estrelas do repositório por dia: 
Arquivo que possui a informação de quantas estrelas o repositório X possui na data Y. Informações desde a criação do repositório até a data de 31/05/2019.

###### Criação
1. Executar no BIGQUERY a QUERY 2 do arquivo consultas_big_query/BIGQUERY-Consultas-GHTorrent. Essa query vai retornar a quantidade de estrelas por dia de cada um dos repositórios selecionados. Baixe o arquivo JSON do resultado no seu Google Drive.
2. Executar o módulo **transformar_created_at_em_data.py** (leitura 2) com o arquivo gerado acima. Esse módulo vai transformar o arquivo em formato JSON lista.
3. Executar o módulo **identifica_data_criacao_repositorio.py** com o arquivo gerado acima e o arquivo JSON que possui os repositórios.
4. Executar o módulo **gerar_historico_estrelas.py** com o arquivo resultado do passo anterior.


##### Histórico de quantidade de forks do repositório por dia: 
Arquivo que possui a informação de quantos forks o repositório X possui na data Y. Informações desde a criação do repositório até a data de 31/05/2019.

###### Criação
1. Executar no BIGQUERY a QUERY 3 do arquivo consultas_big_query/BIGQUERY-Consultas-GHTorrent. Essa query vai retornar a quantidade de forks por dia de cada um dos repositórios selecionados. Baixe o arquivo JSON do resultado no seu Google Drive.
2. Executar o módulo **transformar_created_at_em_data.py** (leitura 2) com o arquivo gerado acima. Esse módulo vai transformar o arquivo em formato JSON lista.
3. Executar o módulo **identifica_data_criacao_repositorio.py** com o arquivo gerado acima e o arquivo JSON que possui os repositórios.
4. Executar o módulo **gerar_historico_forks.py** com o arquivo resultado do passo anterior.

##### Histórico de quantidade de contribuidores do repositório por dia: 
Arquivo que possui a informação de quantos contribuidores o repositório X possui na data Y. Informações desde a criação do repositório até a data de 31/05/2019.

###### Criação
1. Executar no BIGQUERY a QUERY 5 do arquivo consultas_big_query/BIGQUERY-Consultas-GHTorrent. Essa query vai retornar a quantidade de contribuidores por dia de cada um dos repositórios selecionados. Baixe o arquivo JSON do resultado no seu Google Drive.
2. Executar o módulo **transformar_created_at_em_data.py** (leitura 2) com o arquivo gerado acima. Esse módulo vai transformar o arquivo em formato JSON lista.
3. Executar o módulo **identifica_data_criacao_repositorio.py** com o arquivo gerado acima e o arquivo JSON que possui os repositórios.
4. Executar o módulo **gerar_historico_contribuidores.py** com o arquivo resultado do passo anterior.

##### Histórico de quantidade de releases do repositório por dia: 
1. consulta_releases_repositorios.py -> seleciona_releases_entre_datas.py -> gerar_repositorio_data_release.py -> gerar_quantidade_releases_somado_por_dia.py -> identifica_data_criacao_repositorio.py -> gerar_historico_releases.py