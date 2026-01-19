Atividade realizada no curso rápido de Automação de Tarefas com Python pela empresa Hashtag Treinamentos
Consiste em receber uma base de dados de produtos e subir as informações de cada produto no site da empresa, desde o apertar a tecla windows até finalizar a alimentação do site com os dados da base.

A seguir estão as anotações da aula com a base do algoritmo desenvolvidos

Como eu faria pra resolver esse problema manualmente?(passo a passo do programa resumido)

    Passo 1: entrar no sistema da empresa (abrir navegadoe, site da empresa..)
    Passo 2: fazer login
    Passo 3: abrir a base de dados pra saber quais produtos cadastrar
    Passo 4: cadastrar o primeiro produto
    %asso 5: repetir passo 4 até acabar a lista de produtos

- Traduzir cada passo em python

- instalar a biblioteca pyautogui no terminal command prompt "pip install pyautogui"
- Importar as bibliotecas pyautogui, time e pandas

- Lembretes de ações do pyautogui para este projeto
#pyautogui.click #clicar
#pyautogui.write #escrever texto
#pyautogui.press #apertar tecla
#pyautogui.hotkey #aperta um atalho

- colocar uma pausa entre uma ação e outra para evitar travamento no projeto(= 0.5 SEGUNDO)
- criar uma variável para o link do site da empresa

* PASSO 1
    - abrir navegador
    - abrir o chrome
    - apertar enter

* PASSO 2
    - digitar o site
    - pressionar enter
    - fazer uma pausa maior nesse trecho do programa, porque depende da velocidade da internet
    - clicar no campo de email
    - procurar as cordenadas do campo a ser clicado (x, y)
    - utilizar aba auxiliar.py para rastrear as coordenadas do cursor
    - digitar email para login no site da empresa
    - ir para o campo senha (é possível usar tecla tab)
    - digitar senha para login no site da empresa
    - passar pro botão de enter com tab
    - apertar enter
    - fazer uma pausa para o site carregar

* PASSO 3
    - instalar a biblioteca pandas openpayxl  (cmd)(pip install pandas openpyxl)
    - importar a biblioteca pandas (cabeçalho)
    - criar a variável "tabela"
    - importar os valores do arquivo "produtos.csv" em "tabela" criado para o codigo
    - para importar arquivo com mais de uma aba: pandas.read_excel(sheet_name="aba1")
    - mostrar tabela importada

* PASSO 5

  - for linha in tabela.index:
  - (index indica linha) indentar todas as tarefas a serem repetidas em cada linha da tabela
  - para cada item dentro de uma lista de itens

* PASSO 4
    - cadastrar primeiro produto
    - codigo
    - clicar no campo codigo
    - digitar o codigo do primeiro produto
    - criar a variavel "codigo" e indicar para localizar na tabela o item na linha "linha" e coluna "codigo"
    - transformar em texto (str) (todas as variaveis criadas a partir daqui)
    - ir para proximo campo - marca
    - inserir a marca
    - criar a variavel "marca" e indicar para localizar na tabela o item na linha "linha" e coluna "marca"
    - transformar em texto (str)
    - passar para prox campo
    - inserir o tipo
    - transformar em texto (str)
    - passar para prox campo
    - inserir a categoria
    - transformar em texto (str)
    - passar para prox campo
    - inserir o preco_unitario
    - transformar em texto (str)
    - passar para prox campo
    - #inserir o custo
    - transformar em texto (str)
    - passar para prox campo
    - inserir o obs
    - transformar em texto (str)
    - if obs != "nan": #se obs for diferente de NaN, então escrever o valor
    - passar para prox campo - enviar
    - enter em enviar
    - voltar para o início da tela
    - ou press em "home" ou pyautogui.scroll() positivo pixels para cima, negativo pixels para baixo

#PASSO 5 já no passo 4
    #repetir passo 4 para cada produto (cada produto é uma linha na base de dados)
    #"for linha in tabela.index:" colocado acima do passo 4
    # nan = NAN = Not a Number = vazio
