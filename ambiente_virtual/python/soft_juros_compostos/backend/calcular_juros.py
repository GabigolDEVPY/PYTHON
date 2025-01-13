from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

def calcular_juros(valor_inicial, taxa_juros, tipo_juros, valor_investido_meses, meses, anual_ou_mensal, texto, lista, lista_final):
    if anual_ou_mensal == "Anos":
        meses = meses * 12

    # Configurando a fonte da QListWidget para monoespaçada
    fonte_mono = QFont("Courier", 10)  # Escolha monoespaçada para alinhamento correto
    lista.setFont(fonte_mono)
    valor_investido = valor_inicial
    valor_juros = 0
    valor_final = valor_inicial

    # Ajuste para tipo de juros "Anual"
    if tipo_juros == "Anual":
        taxa_juros = (1 + taxa_juros / 100) ** (1 / 12) - 1

    # Título formatado
    texto.setText(" Mês           Juros               Total Investido       Total Juros            Total Acumulado")

    for mes in range(1, meses + 1):
        if tipo_juros == "Anual":
            juros = valor_final * taxa_juros
        else:
            juros = (valor_final / 100) * taxa_juros

        valor_juros += juros
        valor_final += juros + valor_investido_meses

        # Formatando o mês e os valores com espaçamento fixo
        mes_formatado = str(mes).ljust(7)  # 10 caracteres para o mês
        juros_formatado = f"R$ {juros:.2f}".ljust(14)  # 15 caracteres para juros
        investido_formatado = f"R$ {valor_investido:.2f}".ljust(14)  # 15 caracteres para investido
        total_juros_formatado = f"R$ {valor_juros:.2f}".ljust(14)  # 15 caracteres para total juros
        total_acumulado_formatado = f"R$ {valor_final:.2f}".ljust(14)  # 15 caracteres para total acumulado
        valor_investido += valor_investido_meses

        # Montando a linha final
        linha = f"{mes_formatado}{juros_formatado}{investido_formatado}{total_juros_formatado}{total_acumulado_formatado}"

        # Adicionando na QListWidget
        lista.addItem(linha)
        lista_final.setText(f" \n"
                            f"VALOR INVESTIDO:  R${valor_investido}     VALOR JUROS:  {total_juros_formatado} VALOR TOTAL:  {total_acumulado_formatado}")