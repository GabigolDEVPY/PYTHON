from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


def calcular_juros(valor_inicial, taxa_juros, tipo_juros, valor_investido_meses, meses, anual_ou_mensal, texto):
    if anual_ou_mensal == "Anos":
        meses = (meses * 12) 
    if tipo_juros == "Anual":
        taxa_juros = (1 + taxa_juros / 100) ** (1 / 12) - 1
    valor_juros = 0
    valor_final = valor_inicial
    
    for _ in range(meses):
        juros = valor_final * taxa_juros
        valor_juros += juros
        valor_final += juros 
        valor_final += valor_investido_meses
        
    texto.setText(f" TOTAL:   R$ {valor_final:.2f}\n"
                f" JUROS:   R$ {valor_juros:.2f}\n"
                f" VALOR TOTAL INVESTIDO:  R$ {valor_inicial + (valor_investido_meses * meses):.2f}")
    
    
