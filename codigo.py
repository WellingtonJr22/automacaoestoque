#Passo a Passo do projeto 
# Passo 1: Entrar no sistema da empresa 
  #https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pip install pyautogui 
import pyautogui
import time


pyautogui.PAUSE = 15
#pyautogui.click - clicar em algum lugar da tela
#pyautogui.write - escrever um texto
#pyautogui.press - precionar 1 tecla do teclado 

#abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no site 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# dar uma pausa um pouco maior(3 segundos)
time.sleep(10)


# Passo 2: Fazer Login
pyautogui.click(x=785, y=467)
pyautogui.write("wellington.vieirajr23@gmail.com")

#escrever a senha
pyautogui.press("tab")
pyautogui.write("junior1523")

#clicar no botão de logar
pyautogui.click(x=946, y=666)
time.sleep(10)

# Passo 3: Importar a base de dados
#pip install pandas numpy openpyxl
import pandas 
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
# para cada linha da minha tabela
for linha in tabela.index:       
  #clicar no 1° campo
  pyautogui.click(x=628, y=322)
  #codigo do produto 
  codigo = tabela.loc[linha, "codigo"]
  pyautogui.write(codigo)
  pyautogui.press("tab")
  #marca
  pyautogui.write(tabela.loc[linha, "marca"])
  pyautogui.press("tab")
  #tipo
  pyautogui.write(tabela.loc[linha, "tipo"])
  pyautogui.press("tab")
  #categoria
  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")
  #preco
  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")
  #custo
  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")
  #obs
  obs = tabela.loc[linha, "obs"]
  if not pandas.isna(obs): 
   pyautogui.write(tabela.loc[linha, "obs"])
  pyautogui.press("tab")

  pyautogui.press("enter")
  pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até acabar
