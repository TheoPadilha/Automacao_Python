# Passo a passo do projeto

# 1.Abrir sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Para instalar: pip install pyautogui
import pyautogui
import time

# pyautogui.click -> clicar co o mouse.
# pyautigui.write -> escrever um texto.
# pyautogui.press -> pressionar uma tecla dp teclado.
# pyautogui.hotkey -> apertar um conjunto de teclas (Ctrl C,Ctr V,Alt Tab)

pyautogui.PAUSE = 0.5

# Abrir o navegador(opera)
pyautogui.press('win')

pyautogui.write('opera')

pyautogui.press('enter')

# Entrar no site do sistema
time.sleep(2)

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

pyautogui.press('enter')

# aqui ele pode demorar alguns segundos
time.sleep(1)


# 2.Fazer login
pyautogui.click(x=704, y=451)
pyautogui.write('theohenriquecp@gmail.com')

pyautogui.press('tab') # passou para o campo de senha
pyautogui.write('256310@Tp')

pyautogui.press('tab')# passou para o botão de Login 
pyautogui.press('enter')

# 3.Abrir/importar base de dados de cada produto para cadastrar 
# pip install pandas , numpy, openpyxl
import pandas as pd
tabela = pd.read_csv('NOVO/produtos.csv')
                                   
#print(tabela)

# 4.Cadastrar um produto 
time.sleep(2)

for linha in tabela.index:
    
    codigo = str(tabela.loc[linha , 'codigo'])
    marca = (str(tabela.loc[linha , 'marca']))
    tipo = (str(tabela.loc[linha , 'tipo']))
    categoria = (str(tabela.loc[linha , 'categoria']))
    preço = (str(tabela.loc[linha , 'preco_unitario']))
    custo = (str(tabela.loc[linha , 'custo']))
    obs = (str(tabela.loc[linha , 'obs']))
        
    #clicar no campo do codigo do produto
    pyautogui.click(x=787, y=296)

    #preencher o codigo
    pyautogui.write(codigo)                  #(str(tabela.loc[linha , 'codigo']))

    #passar para o proximo campo
    pyautogui.press('tab')

    #preencher a marca
    pyautogui.write(marca)                   #(str(tabela.loc[linha , 'marca']))

    #passar para o proximo campo
    pyautogui.press('tab')

    #preencher o tipo
    pyautogui.write(tipo)                    #(str(tabela.loc[linha , 'tipo']))

    #passar para o proximo campo
    pyautogui.press('tab')

    #preencher a categoria
    pyautogui.write(categoria)               #(str(tabela.loc[linha , 'categoria']))

    #passar para o proximo campo
    pyautogui.press('tab')

    #preencher o preço
    pyautogui.write(preço)                   #(str(tabela.loc[linha , 'preco_unitario']))

    #passar para o proximo campo
    pyautogui.press('tab')

    #preencher o custo
    pyautogui.write(custo)                   #(str(tabela.loc[linha , 'custo']))


    #passar para o proximo campo
    pyautogui.press('tab')

    #preencher a obs
    if obs != 'nan':
        pyautogui.write(obs)                     #(str(tabela.loc[linha , 'obs']))
        
    #passar para o proximo campo
    pyautogui.press('tab')

    #clicar em enviar 
    pyautogui.press('enter')
    
    #voltar ao inicio da tela
    pyautogui.scroll(5000)
    

# 5.Repetir o processo até acabar a lista de produtos 