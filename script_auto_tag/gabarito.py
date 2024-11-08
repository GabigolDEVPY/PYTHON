# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

pyautogui.PAUSE = 0.1

tags_roupas = [
    "Casual",
    "Formal",
    "Esporte",
    "Streetwear",
    "Verão",
    "Inverno",
    "Outono",
    "Primavera",
    "Clássico",
    "Moderno",
    "Minimalista",
    "Fashion",
    "Sustentável",
    "Vintage",
    "Confortável",
    "Luxo",
    "Boho",
    "Urbano",
    "Executivo",
    "Trabalho",
    "Festa",
    "Casamento",
    "Passeio",
    "Férias",
    "Academia",
    "Básico",
    "Elegante",
    "Despojado",
    "Unissex",
    "Alta Costura"
]




# # Passo 4: Cadastrar um produto
pyautogui.click(x=946, y=1052)
for linha in tags_roupas:
    pyautogui.click(x=613, y=1005)
    pyautogui.click(x=613, y=1005)
    pyautogui.write(linha)
    pyautogui.press('enter')
    




