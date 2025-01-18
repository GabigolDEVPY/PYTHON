from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import tela_inicial_interface
import requests
import sys


janela_login = None

def tela():
    app = QApplication(sys.argv)
    global janela_login
    janela_login = QMainWindow()
    central_widget = QWidget()
    janela_login.setCentralWidget(central_widget)
    layout_principal = QVBoxLayout()
    central_widget.setLayout(layout_principal)
    
    # linha login
    texto_login = QLabel("LOGIN")
    linha_login = QLineEdit()
    linha_login.setMinimumSize(350, 34)
    
    # linha senha
    texto_senha = QLabel("SENHA")
    linha_senha = QLineEdit()
    linha_senha.setMinimumSize(350, 34)
    
    # criando botão login
    botao_login = QPushButton("LOGIN")
    botao_login.setMinimumSize(350, 34)
    
    
    # criando botão register
    botao_register = QPushButton("REGISTRAR")
    botao_register.setMinimumSize(350, 34)
    
    caixa = QLabel()
    
    layout_principal.addWidget(texto_login)
    layout_principal.addWidget(linha_login)
    layout_principal.addWidget(texto_senha)
    layout_principal.addWidget(linha_senha)
    layout_principal.addWidget(botao_login)
    layout_principal.addWidget(botao_register)
    layout_principal.addWidget(caixa)
    
    #acessar o servidor
    
    def acessar_servidor_login():
        login = linha_login.text()
        senha = linha_senha.text()
        print("deu certo")
        url = f"http://localhost:5000/login/login={login}&senha={senha}"
        result = requests.get(url)
        if result.status_code == 404:
            return caixa.setText("Usuário não encontrado")
        
        janela_login.close()
        tela_inicial_interface.tela_inicial()  
        caixa.setText(f" Seja Bem-vindo {login} seu saldo é de R$: {result.text}")
        
    def acessar_servidor_registrar():
        login = linha_login.text()
        senha = linha_senha.text()
        saldo = 0
        print("deu certo")

        dados = {
        "login": login,
        "senha": senha,
        "saldo": saldo
        }
        
        url = "http://localhost:5000/register"
        result = requests.put(url, json=dados)
        print(result)
        if result.status_code == 500:
            caixa.setText("User registered")
    
    
    botao_login.clicked.connect(lambda: acessar_servidor_login())
    
    botao_register.clicked.connect(lambda: acessar_servidor_registrar())
    
    
    #dsd
    janela_login.show()
    app.exec()
    
tela()    