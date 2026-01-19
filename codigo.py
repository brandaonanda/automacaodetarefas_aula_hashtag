#como eu faria pra resolver esse problema manualmente?(passo a passo do programa)

    # passo 1: entrar no sistema da empresa (abrir navegadoe, site da empresa..)
    # passo 2: fazer login
    # passo 3: abrir a base de dados pra saber quais produtos cadastrar
    # passo 4: cadastrar o primeiro produto
    # passo 5: repetir passo 4 até acabar a lista de produtos

#traduzir cada passo em python
#PAUSAR AUTOMAÇÃO = LEVAR O CURSOR ATÉ O PONTO SUPERIOR ESQUERDO DA TELA

#bibliotecas = pacotes de codigo
#instalar pyautogui no terminal command prompt "pip install pyautogui"

import pyautogui
import time #para esperar um pouco mais em momentos especificos
import pandas #para ler a base de dados (importar o arquivo)

#pyautogui.click #clicar
#pyautogui.write #escrever texto
#pyautogui.press #apertar tecla
#pyautogui.hotkey #aperta um atalho

#colocar uma pausa entre uma ação e outra para evitar travamento (= 0.5 SEGUNDO)
pyautogui.PAUSE = 0.5
#criar uma variável (link)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#PASSO 1
    #abrir navegador
pyautogui.press("win")
    #abrir o chrome
pyautogui.write("chrome")
    #apertar enter
pyautogui.press("enter")

#PASSO 2
    #digitar o site
pyautogui.write(link) #sem aspas pq é valor e não texto
    #dar enter
pyautogui.press("enter") 
    #fazer uma pausa maior pq depende da velocidade da internet
    #import time - cabeçalho
time.sleep(3) #3 segundos de espera #pyautogui hashtag no youtube
    #clicar no campo de email
    #procurar as cordenadas do campo a ser clicado (x, y)
    #aba auxiliar.py
pyautogui.click(x=684, y=569) #visto na aba auxiliar.py
    #digitar email
pyautogui.write("pythonimpressionador@gmail.com")
    #ir para o campo senha (é possível usar tecla tab)
pyautogui.press("tab")
    #digitar senha
pyautogui.write("shsq8wyeq9wd0qwhd90q")
    #passar pro botao de enter
pyautogui.press("tab")
    #apertar enter
pyautogui.press("enter")
    #fazer uma pausa pro site carregar
time.sleep(4)

#PASSO 3
    #instalar a biblioteca pandas openpayxl  (cmd)(pip install pandas openpyxl)
    #importar a biblioteca pandas (cabeçalho)
    #criar "tabela"
tabela = pandas.read_csv("produtos.csv") #importar os valores do arquivo "produtos.csv" em "tabela" criado para o codigo
    #para importar arquivo com mais de uma aba: pandas.read_excel(sheet_name="aba1")
print(tabela)

    #PASSO 5
for linha in tabela.index: # (index indica linha) indentar todas as tarefas a serem repetidas em cada linha da tabela
#para cada item dentro de uma lista de itens

#PASSO 4
    #cadastrar primeiro produto
    #codigo
    #clicar no campo codigo
    pyautogui.click(x=672, y=382)
        #digitar o codigo do primeiro produto
        #criar a variavel "codigo" e indicar para localizar na tabela o item na linha "linha" e coluna "codigo"
    codigo = str(tabela.loc[linha, "codigo"]) #transformar em texto (str)
    pyautogui.write(codigo)
        #ir para proximo campo - marca
    pyautogui.press("tab")
        #inserir a marca
        #criar a variavel "marca" e indicar para localizar na tabela o item na linha "linha" e coluna "marca"
    marca =str(tabela.loc[linha, "marca"]) #transformar em texto (str)
    pyautogui.write(marca)
        #passar para prox campo
    pyautogui.press("tab")
        #inserir o tipo
        #criar a variavel "tipo" e indicar para localizar na tabela o item na linha "linha" e coluna "tipo"
    tipo = str(tabela.loc[linha, "tipo"]) #transformar em texto (str)
    pyautogui.write(tipo)
        #passar para prox campo
    pyautogui.press("tab")
        #inserir a categoria
        #criar a variavel "categoria" e indicar para localizar na tabela o item na linha "linha" e coluna "categoria"
    categoria = str(tabela.loc[linha, "categoria"]) #transformar em texto (str)
    pyautogui.write(categoria)
        #passar para prox campo
    pyautogui.press("tab")
        #inserir o preco_unitario
        #criar a variavel "preco_unitario" e indicar para localizar na tabela o item na linha "linha" e coluna "preco_unitario"
    preco_unitario = str(tabela.loc[linha, "preco_unitario"]) #transformar em texto (str)
    pyautogui.write(preco_unitario)
        #passar para prox campo
    pyautogui.press("tab")
        #inserir o custo
        #criar a variavel "custo" e indicar para localizar na tabela o item na linha "linha" e coluna "custo"
    custo = str(tabela.loc[linha, "custo"]) #transformar em texto (str)
    pyautogui.write(custo)
        #passar para prox campo
    pyautogui.press("tab")
        #inserir o obs
        #criar a variavel "obs" e indicar para localizar na tabela o item na linha "linha" e coluna "obs"
    obs = str(tabela.loc[linha, "obs"]) #transformar em texto (str)
    if obs != "nan": #se obs for diferente de NaN, então escrever o valor
        pyautogui.write(obs) #identado
        #passar para prox campo - enviar
    pyautogui.press("tab")
        #enter em enviar
    pyautogui.press("enter")
        #voltar para o início da tela
    pyautogui.press("home") #ou press em "home" ou pyautogui.scroll() positivo pixels para cima, negativo pixels para baixo

#PASSO 5
    #repetir passo 4 para cada produto (cada produto é uma linha na base de dados)
    #"for linha in tabela.index:" colocado acima do passo 4
    # nan = NAN = Not a Number = vazio