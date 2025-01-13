from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


def calcular_juros(valor_inicial, taxa_juros, tipo_juros, valor_investido_meses, meses, texto):
    valor_juros = 0
    valor_final = valor_inicial
    for _ in range(meses):
        juros = ((valor_final / 100) * taxa_juros)
        valor_juros += juros
        valor_final += juros
        valor_final += valor_investido_meses
    print(valor_final)
    texto.setText(f"TOTAL:   {valor_final:.2f}\n"
                f"JUROS:   {valor_juros:.2f}\n"
                f"VALOR TOTAL INVESTIDO:   {valor_inicial + (valor_investido_meses * meses):.2f}")