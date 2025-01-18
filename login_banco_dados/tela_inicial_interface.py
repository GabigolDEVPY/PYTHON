from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import requests
import sys

janela_inicial = None

def tela_inicial():
    global janela_inicial
    janela_inicial = QMainWindow()
    central_widget = QWidget()
    janela_inicial.setCentralWidget(central_widget)
    layout_principal = QVBoxLayout()
    central_widget.setLayout(layout_principal)
    
    janela_inicial.show()