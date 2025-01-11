from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from python.soft_juros_compostos.backend.calcular_juros import calcular_juros
import sys

def tela():
    window = QMainWindow() #tela principal 
    window.setFixedSize(500, 300) #ajustando tamanho fixo tela principal
    central_widget = QWidget()      #widget central
    layout = QVBoxLayout() # layout de todos
    central_widget.setLayout(layout)     #centra_widget
    window.setCentralWidget(central_widget)
    button = QPushButton("CALCULAR")    #botão calcular
    button.setFixedSize(483, 40)
    
    # layout dos lados
    layout_lados = QHBoxLayout()
    
    #layout lado esquerdo
    layout_1 = QVBoxLayout()
    linha_texto_valor = QLabel("VALOR")
    linha_valor_inicial = QLineEdit()
    linha_valor_inicial.setFixedSize(235, 30)
    linha_valor_inicial.setPlaceholderText("00,00")
    linha_taxa_juros = QLabel("TAXA DE JUROS")
    taxa_de_juros = QLineEdit()
    taxa_de_juros.setFixedSize(235, 30)
    taxa_de_juros.setPlaceholderText("8,00")
    
    # adicionando o widgets layout esquerdo
    layout_1.addWidget(linha_texto_valor)
    layout_1.addWidget(linha_valor_inicial)
    layout_1.addWidget(linha_taxa_juros)
    layout_1.addWidget(taxa_de_juros)
    layout_lados.addLayout(layout_1)
    
    #layout lado direito
    layout_2 = QVBoxLayout()
    linha_texto_valor_mensal = QLabel("VALOR MENSAL")
    linha_valor_mensal = QLineEdit()
    linha_valor_mensal.setFixedSize(235, 30)
    linha_valor_mensal.setPlaceholderText("00,00")
    linha_periodo = QLabel("PERÍODO")
    periodo = QLineEdit()
    periodo.setFixedSize(235, 30)
    periodo.setPlaceholderText("8,00")
    
    # adicionando o widgets layout esquerdo
    layout_2.addWidget(linha_texto_valor_mensal)
    layout_2.addWidget(linha_valor_mensal)
    layout_2.addWidget(linha_periodo)
    layout_2.addWidget(periodo)
    layout_lados.addLayout(layout_2)
    
    # informações centrais/resultado etc
    texto_central = QLabel()
    texto_central.setStyleSheet("font-size: 14px ;")
    
    # adicionado layout, botoes e texto central no layout principal
    layout.addLayout(layout_lados)
    layout.addWidget(texto_central)
    layout.addWidget(button)
    
    
    button.clicked.connect(lambda: calcular_juros(float(linha_valor_inicial.text()), float(taxa_de_juros.text()), float(linha_valor_mensal.text()), int(periodo.text()), texto_central))
    
    
    window.show()
    app.exec()


app = QApplication(sys.argv)
tela()


