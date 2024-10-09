import json

ARQUIVO_DINHEIRO = 'dados.json'

def carregar_dinheiro():
    try:
        with open(ARQUIVO_DINHEIRO, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

def salvar_dinheiro(valor):
    with open(ARQUIVO_DINHEIRO, 'w') as f:
        json.dump(valor, f)

# Carrega o dinheiro ao iniciar o programa
meu_dinheiro = carregar_dinheiro()
