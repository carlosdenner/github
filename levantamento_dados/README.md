# LEVANTAMENTO DE DADOS GITHUB

## Processos para acessar dados do Github utilizando a API de REST do GitHub. Esses dados servirão como base para realizar análises de fins acadêmicos.

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
- **consulta_repositorios.py**: recebe como entrada as palavras-chave que deseja pesquisa e seus respectivos valores. Exemplo: Deseja pesquisa repositórios com o tópico open-data, então deve ser informado palavra-chave = topic e valor palavra-chave = open-data. Sua saída é um arquivo JSON com o seguinte formato: palavras-chave:valor palavra-chave-timestamp.json (topic:open-data-2021-06-19T10:23:38.811947.json).
- **atualiza_base.py**: atualiza o arquivo JSON central chamado base_dados_repositorios.json. Recebe como entrada um arquivo contruido no consulta_repositorio.py e verifica repositório a repositório. Caso o repositório exista na base de dados faz atualização, caso não exista inclui na base de dados.
- **visualiza_dados.py**: recebe como entrada o arquivo central base de dados e faz análises com suas informações. Gera como saída gráficos em um arquivo html chamado analise_dados.html.

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python3](https://www.python.org/)
- [JSON](https://www.json.org/json-en.html)


