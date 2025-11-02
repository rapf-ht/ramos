import pyautogui
# pyautogui.click - clicar em algum lugar 
# pyautogui.press - apertar 1 tecla
# pyautogui.write - escrever um texto
# pyautogui.hotkey - apertar uma combinação de teclas

# Entrando no navegador
pyautogui.PAUSE = 0.3
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=803, y=639)

# Entrando no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

import time

time.sleep(3)
pyautogui.click(x=858, y=470)
pyautogui.write("zicagames@gmail.com")
pyautogui.press("tab")
pyautogui.write("*************************")
pyautogui.press("enter")

import pandas as pd # Apelido ao pandas -> pd

tabela = pd.read_csv("D:/Python/Intensivo Python/Automação/produtos.csv")

time.sleep(0.5)

# Escrever a primeira leva
# Usando o pandas para acessar o banco de dados

for linha in tabela.index:
    pyautogui.click(x=709, y=332)
    pyautogui.hotkey("ctrl", "a")
    cod = (str(tabela.loc[linha, "codigo"]))
    pyautogui.write(cod)

    pyautogui.press("tab")

    marca = (str(tabela.loc[linha, "marca"]))
    pyautogui.write(marca)

    pyautogui.press("tab")

    disp = (str(tabela.loc[linha, "tipo"]))
    pyautogui.write(str(disp))

    pyautogui.press("tab")
    
    cat = (str(tabela.loc[linha, "categoria"]))
    pyautogui.write(str(cat))

    pyautogui.press("tab")
    
    preco = (str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = (str(tabela.loc[linha, "custo"]))
    pyautogui.write(custo)

    # Scroll

    pyautogui.scroll(-1000)

    pyautogui.press("tab")
    
    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan" or "NaN":
        obs = "-"
    pyautogui.write(obs)

    time.sleep(0.2)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("enter") # Enter novamente, site não funciona direito
    pyautogui.scroll(10000) # Finalizando o processo