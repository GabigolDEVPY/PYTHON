from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import requests  # Para enviar requisições ao servidor


def janela():
    app = QApplication(sys.argv)
    app.setStyle("Windows11")

    # Configurando a janela principal
    window = QMainWindow()
    central_Widget = QWidget()
    window.setCentralWidget(central_Widget)
    layout_central = QVBoxLayout()  # Layout central
    central_Widget.setLayout(layout_central)

    # Criando widgets
    busca = QLineEdit()
    busca.setMinimumSize(300, 25)
    busca.setStyleSheet("font-size: 20px; border: 2px solid #00ffff; border-radius: 4px;")
    busca.setPlaceholderText("Digite o nome para buscar")

    buton = QPushButton("Buscar")
    buton.setMinimumSize(310, 40)

    resultados = QListWidget()

    # Adicionando widgets ao layout
    layout_central.addWidget(busca)
    layout_central.addWidget(resultados)
    layout_central.addWidget(buton)

    # Função para buscar no servidor
    def buscar_no_servidor():
        nome = busca.text().strip()
        if not nome:
            resultados.clear()
            resultados.addItem("⚠️ Por favor, digite um nome!")
            return

        try:
            url = f"http://127.0.0.1:5000/buscar?nome={nome}"
            resposta = requests.get(url)

            if resposta.status_code == 200:
                dados = resposta.json()
                resultados.clear()
                for chave, valor in dados[nome].items():
                    resultados.addItem(f"{chave}: {valor}")
            else:
                resultados.clear()
                resultados.addItem("⚠️ Nome não encontrado no servidor!")

        except Exception as e:
            resultados.clear()
            resultados.addItem(f"❌ Erro ao se conectar ao servidor: {e}")

    # Conectando o botão à função
    buton.clicked.connect(buscar_no_servidor)

    # Exibindo a janela
    window.setWindowTitle("Busca no Servidor")
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())


janela()