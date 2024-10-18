import json
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DADOS = os.path.join(BASE_DIR, 'dados.json')
ARQUIVO_PALAVRAS = os.path.join(BASE_DIR, 'lista_palavras.json')

# Função para carregar a lista de palavras
def carregar_lista():
    try:
        with open(ARQUIVO_PALAVRAS, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Retorna uma lista vazia se o arquivo não existir

# Função para limpar a tela
def limpar():
    os.system('cls')

lista = carregar_lista()

# Função para carregar dados do arquivo JSON
def carregar_dados():
    try:
        with open(DADOS, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou estiver corrompido, retorna o dicionário padrão
        return {"meu_dinheiro": 10, "carros": [], "casas": [], "perifericos": [{"item": "Teclado", "Valor": "500"}]}


# Função genérica para salvar qualquer tipo de dado no arquivo JSON
def salvar_dados(chave, valor):
    dados = carregar_dados()  # Carrega os dados atuais
    dados[chave] = valor      # Atualiza o valor da chave passada
    with open(DADOS, 'w') as f:
        json.dump(dados, f, indent=4)  # Salva o dicionário atualizado

# Carrega os dados ao iniciar o programa
dados = carregar_dados()

def ver_inventario(itens):
    for i, item in enumerate(itens):
        print(f'{i}: {item["item"]} - Valor: {item["Valor"]}')
    time.sleep(3)
