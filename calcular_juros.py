from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


def calcular_juros(valor_inicial, taxa_juros, valor_investido_meses, meses):
    valor_final = valor_inicial
    for _ in range(meses):
        juros = ((valor_final / 100) * taxa_juros)
        valor_final += juros
        valor_final += valor_investido_meses
    print(valor_final)
    return valor_final



    