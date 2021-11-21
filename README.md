Este repositório faz parte da pesquisa “Projetos Colaborativos de Software Livre: Estudo da Relação do Processo de Tomada de Decisão e o Sucesso”.

Projetos Colaborativos de Software Livre são modelos extremos de projetos de crowdsourcing bem-sucedidos, no centro destes está o processo de tomada de decisão (PTD). Contudo, poucas pesquisas investigam PTD entorno da codificação de software. Nesta pesquisa, investigaremos – por meio de estudos quantitativos – a correlação entre o sucesso do projeto e características da participação no PTD. Verificaremos se há correlação entre as variáveis sucesso do projeto e a quantidade de contribuidores dos Episódio de Tomada de Decisão (ETD), e se há correlação entre o sucesso do projeto e o nível de experiência dos constribuidores. 

Os dados analisados são oriundos do dataset do GHTorrent, que possui dados de fevereiro de 2012 a junho de 2019 de repositórios hospedados no GitHub, e da API REST do GitHub, que é um conjunto de definições e protocolos que possibilita a integração de aplicações. Primeiro, utilizando o dataset do GHTorrent,  para realizar uma análise da trajetória desde o início da criação do repositório, foram identificados todos os repositórios da linguagem python, que iniciaram a partir de fevereiro de 2012 a junho de 2019, foram identificados 718.173 repositórios. Em seguida, estes repositórios foram ordenados em função da quantidade de estrelas que eles possuíam em junho de 2019, e foi selecionada uma amostra com os 1000 repositórios com maior quantidade de estrelas. Com base na literatura de referência, propusemos os indicadores que compõem as três variáveis de pesquisa. A primeira variável é o sucesso do projeto que será mensurado pela quantidade de linhas de código alteradas, estrelas, forks e releases; a segunda variável é a quantidade de contribuidores do ETD que é o somatório dos contribuidores que atuaram em um pull request (PR) ou em um issue ou commit associado ao PR; e, a terceira é o nível de experiência dos contribuidores, que serão medidos a partir da data da primeira colaboração em um ETD e da quantidade de colaboração em ETD.

Durante a análise dos dados foi identificado que 333 repositórios não possuíam releases, por este motivo decidimos retirar esses repositórios do histórico geral de indicadores, pois a ausência desta informação afetará o cálculo do escore de sucesso. Dessa forma, esta base de dados possui dados de 667 repositórios.

Os arquivos estão no formato JSON, e possuem a seguinte estrutura:

historico-geral-de-indicadores-com-releases 
{
    "id":"367",  id do repositório
    "data":"02-08-2012",
    "estrelas":180,
    "forks":1,
    "releases":0,
    "linhas_alteradas":73628
  },
  
contribuidores-pull-request
  {
    "id_pull_request":"229034",
    "repo_id":"367",
    "id_contribuidor":"2376",
    "data":"02-08-2012"
  },

historico-contribuidor-data-inicio-github
{
    "id":"6",  id do contribuidor
    "data":"05-02-2010"
  },
historico-contribuidor-data-inicio-projeto
{
    "repo_id":"367",
    "id_contribuidor":"11",
    "data":"30-11-2017"
  },
quantidade-contribuidores-por-dia
{
    "id":"367",
    "data":"02-08-2012",
    "contribuidores":1
  },
