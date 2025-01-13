from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from python.soft_juros_compostos.backend.calcular_juros import calcular_juros
import sys

def tela():
    window = QMainWindow() #tela principal 
    window.setFixedSize(540, 450) #ajustando tamanho fixo tela principal
    window.setWindowTitle("CALCULADORA DE JUROS COMPOSTOS")
    central_widget = QWidget()      #widget central
    layout = QVBoxLayout() # layout de todos
    central_widget.setLayout(layout)     #centra_widget
    window.setCentralWidget(central_widget)
    button = QPushButton("CALCULAR")    #botão calcular
    button.setStyleSheet("QPushButton:hover {font-size: 14px; background-color: #aa4000;  color: #ffffff; }")
    button.setFixedSize(520, 40)
    button_limpar = QPushButton("LIMPAR")    #botão calcular
    button_limpar.setFixedSize(520, 40)
    button_limpar.setStyleSheet("QPushButton:hover {font-size: 14px; background-color: #910000;  color: #ffffff; }")

    titulo = QLabel(" CALCULADORA DE JUROS COMPOSTOS\n"
                    "    ")
    titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
    
    
    # layout dos lados
    layout_lados = QHBoxLayout() #criando layout para colocar lado esquerdo e direito
    
    # criando widgets layout lado esquerdo
    layout_1 = QVBoxLayout()   #layout do lado esquerdo
    linha_texto_valor = QLabel("VALOR")
    linha_valor_inicial = QLineEdit()
    linha_valor_inicial.setFixedSize(245, 30)  #setando tamanho fixo da linha
    linha_valor_inicial.setPlaceholderText("00,00")
    linha_taxa_juros = QLabel("TAXA DE JUROS")
    taxa_de_juros = QLineEdit() # taxa de juros, linha para inserir
    taxa_de_juros.setFixedSize(180, 30)
    taxa_de_juros.setPlaceholderText("8,00")
    
    tipo_de_juros = QComboBox() # criando caixa de seleção de opção juros
    tipo_de_juros.setFixedSize(65, 30)
    tipo_de_juros.setStyleSheet("QComboBox:hover {font-size: 14px; background-color: #aa4000;  color: #ffffff; }")
    tipo_de_juros.addItems(["Mensal", "Anual"])

    
    
    
    # layout esquerdo para linha juros e tipo mensal ou anual
    layout_juros_mensal_anual = QHBoxLayout()
    layout_juros_mensal_anual.setSpacing(0)
    layout_juros_mensal_anual.addWidget(taxa_de_juros)
    layout_juros_mensal_anual.addWidget(tipo_de_juros)
    
    
    # adicionando o widgets layout esquerdo
    layout_1.addWidget(linha_texto_valor)
    layout_1.addWidget(linha_valor_inicial)
    layout_1.addWidget(linha_taxa_juros)
    layout_1.addLayout(layout_juros_mensal_anual)
    layout_lados.addLayout(layout_1)
    
    # ________________________________________________________________LAYOUT DIREITO________________________________________________________________________ 
    #layout lado direito
    layout_2 = QVBoxLayout() # criando o layout direito 
    linha_texto_valor_mensal = QLabel("VALOR MENSAL")
    linha_valor_mensal = QLineEdit()
    linha_valor_mensal.setFixedSize(245, 30)
    linha_valor_mensal.setPlaceholderText("00,00")
    linha_periodo = QLabel("PERÍODO")
    periodo = QLineEdit()
    periodo.setFixedSize(180, 30)
    periodo.setPlaceholderText("12")
    
    #criando caixinha de seleção meses, ou anos
    selecao_meses_anual = QComboBox()
    selecao_meses_anual.setFixedSize(65, 30)
    selecao_meses_anual.setStyleSheet("QComboBox:hover {font-size: 14px; background-color: #aa4000;  color: #ffffff; }")
    selecao_meses_anual.addItems(["Meses", "Anos"])
    
    # layout direito para linha juros e tipo mensal ou anual
    layout_meses_anos = QHBoxLayout()
    layout_meses_anos.setSpacing(0)
    layout_meses_anos.addWidget(periodo)
    layout_meses_anos.addWidget(selecao_meses_anual)  #caixinha seleção
    
    
    # adicionando o widgets layout esquerdo
    layout_2.addWidget(linha_texto_valor_mensal)
    layout_2.addWidget(linha_valor_mensal)
    layout_2.addWidget(linha_periodo)
    layout_2.addLayout(layout_meses_anos)
    layout_lados.addLayout(layout_2)
    
    # informações centrais/resultado etc
    lista_informações = QListWidget()
    texto_central = QLabel() #adicionado o campo que será exibida as informações
    texto_central.setStyleSheet("font-size: 14px ;")
    texto_central.setFixedSize(300, 50)
    
    
    
    # adicionado layout, botoes e texto central no layout principal
    layout.addWidget(titulo)
    layout.addLayout(layout_lados)
    layout.addWidget(lista_informações)
    layout.addWidget(texto_central)
    layout.addWidget(button)
    layout.addWidget(button_limpar)
    
    # definindo opção limpar caixas de entrada
    
    button_limpar.clicked.connect(lambda: (linha_valor_inicial.clear(), linha_valor_mensal.clear(), taxa_de_juros.clear(), periodo.clear(), texto_central.clear()))
    button.clicked.connect(lambda: calcular_juros(float(linha_valor_inicial.text()), float(taxa_de_juros.text()), tipo_de_juros.currentText(), float(linha_valor_mensal.text()), int(periodo.text()), selecao_meses_anual.currentText(), texto_central))
    
    
    window.show() # exibindo a tela
    app.exec()


app = QApplication(sys.argv)
app.setStyle("Fusion")
tela()


